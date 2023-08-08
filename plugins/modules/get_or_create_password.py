#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2023, Alban Garrigue <alban@garrigue.me>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
module: get_or_create_password
short_description: Get or create password in Passbolt
description:
    - The Passbolt get_or_create password module try to get a password in Passbolt via the API, if it doesn't exist the module create it.
    - You either need the gpgkey and the passphrase or the fingerprint of the secret key stored in the gpg-agent.    
author: "Alban Garrigue (@albang)"
options:
  passbolt_uri:
    type: str
    required: true
    description:
      - The Passbolt instance Fully Qualified Domain Name(FQDN)
  gpgkey:
    type: str
    required: false
    description:
      - The GPG Private key used to access Passbolt.
  passphrase:
    type: str
    required: false
    description:
      - The Passphrase used with the GPG Private key used to access Passbolt.
  fingerprint:
    description:
      - The fingerprint of the imported Private key used to access Passbolt.
    required: false
  verify:
    description:
      - Whether to verify SSL or not. (Defaults to verify)
    required: false
  name:
    type: str
    required: true
    description:
      - The name of the password you wish to create.
  password:
    type: str
    required: true
    description:
      - The password you wish to create.
  username:
    type: str
    required: false
    description:
      - The username field of the password you wish to create. (Optional but strongly encouraged.)
  uri:
    type: str
    required: false
    description:
      - The uri field of the password you wish to create. (Optional)
  description:
    type: str
    required: false
    description:
      - The description field of the password you wish to create. (Optional)
  encrypt_description:
    type: bool
    required: false
    description:
      - Option to create the password description as a secret and encrypt it in the database. (Optional. Defaults to true.)
    default: True
"""

EXAMPLES = """
- name: Get or create Password
  daniel_lynch.passbolt.get_or_create_password:
    passbolt_uri: "https://passbolt.example.com"
    gpgkey: "{{ gpgkey }}"
    passphrase: "password"
    name: "Testing"
    password: "{{ lookup('ansible.builtin.password', '/dev/null', chars=['ascii_letters', 'digits', 'punctuation']) }}"
    username: "Test"
    uri: "test.com"
    description: "This is a description"
  delegate_to: localhost
  register: get_or_create_password
# You can use it where you want 
- debug:
  msg: "The password is  {{ get_or_create_password.password.password }}"

"""
import traceback

try:
    from ansible.module_utils.basic import AnsibleModule
    from passbolt.passbolt import passbolt
except ImportError:
    HAS_ANOTHER_LIBRARY = False
    ANOTHER_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_ANOTHER_LIBRARY = True
    ANOTHER_LIBRARY_IMPORT_ERROR = False


def main():
    module = AnsibleModule(
        argument_spec=dict(
            passbolt_uri=dict(type='str', required=True, no_log=True),
            gpgkey=dict(type='str', required=False, no_log=True),
            passphrase=dict(type='str', required=False, no_log=True),
            name=dict(type='str', required=True),
            password=dict(type='str', required=True, no_log=False),
            username=dict(type='str', required=False),
            uri=dict(type='str', required=False),
            description=dict(type='str', required=False),
            encrypt_description=dict(type='bool', required=False, default=True),
            fingerprint=dict(type='str', required=False, default=None),
            verify=dict(type='str', required=False, default=True),
        ),
        supports_check_mode=True,
    )

    if not HAS_ANOTHER_LIBRARY:
        module.fail_json(msg="missing lib", exception=ANOTHER_LIBRARY_IMPORT_ERROR)

    passbolt_uri = module.params['passbolt_uri']
    gpgkey = module.params['gpgkey']
    passphrase = module.params['passphrase']
    name = module.params['name']
    password = module.params['password']
    username = module.params['username']
    uri = module.params['uri']
    description = module.params['description']
    encrypt_description = module.params['encrypt_description']
    verify = module.params['verify']
    fingerprint = module.params['fingerprint']

    if type(verify) is str and verify.lower() in ("true", "false"):
        verify = verify.lower() == "true"

    Passbolt = passbolt(apiurl=passbolt_uri, privatekey=gpgkey, passphrase=passphrase, fingerprint=fingerprint,
                        verify=verify)
    existing_password = Passbolt.getpassword(name, username)
    if existing_password:
        changed = False
        module.exit_json(msg="The resource has been retrieved successfully", changed=changed, password=existing_password[0].__dict__)
    else:
        response = Passbolt.createpassword(name, password, username, uri, description, encrypt_description)
        if response == "The resource has been added successfully.":
            existing_password = Passbolt.getpassword(name, username)
            changed = True
            module.exit_json(msg=response, changed=changed,password=existing_password[0].__dict__)
        else:
            changed = False
            module.fail_json(msg=response)


if __name__ == '__main__':
    main()
