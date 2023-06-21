#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2023, Daniel Lynch <daniel.lynch2016@gmail.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
module: update_password
short_description: Update password in Passbolt.
description:
    - The Passbolt update password module updates a password in Passbolt via the API.
    - You either need the gpgkey and the passphrase or the fingerprint of the secret key stored in the gpg-agent.
author: "Daniel Lynch (@daniel-lynch)"
options:
  passbolt_uri:
    type: str
    required: true
    description:
      - The Passbolt instance Fully Qualified Domain Name(FQDN).
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
      - The name of the password you wish to update.
  password:
    type: str
    required: true
    description:
      - The updated password.
  username:
    type: str
    required: false
    description:
      - The username field of the password you wish to update. (Optional but strongly encouraged if there are multiple passwords with the same name.)
  newname:
    type: str
    required: false
    description:
      - The new name of the password you wish to update. (Optional)
  newusername:
    type: str
    required: false
    description:
      - The new username of the password you wish to update. (Optional)
  uri:
    type: str
    required: false
    description:
      - The uri field of the password you wish to update. (Optional)
  description:
    type: str
    required: false
    description:
      - The description field of the password you wish to update. (Optional)
  encrypt_description:
    type: bool
    required: false
    description:
      - Option to create the password description as a secret and encrypt it in the database. (Optional. Defaults to true.)
    default: True
"""

EXAMPLES = """
- name: Update Password
  daniel_lynch.passbolt.update_password:
    passbolt_uri: "https://passbolt.example.com"
    gpgkey: "{{ gpgkey }}"
    passphrase: "password"
    name: "Testing"
    password: "password"
    username: "Test"
    newname: "Testing2"
    newusername: "Test2"
    uri: "test2.com"
    description: "This is a description2"
  delegate_to: localhost

- name: Update Password Using Fingerprint
  daniel_lynch.passbolt.update_password:
    passbolt_uri: "https://passbolt.example.com"
    fingerprint="{{ fingerprint }}"
    name: "Testing"
    password: "password"
    username: "Test"
    newname: "Testing2"
    newusername: "Test2"
    uri: "test2.com"
    description: "This is a description2"
  delegate_to: localhost
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
            password=dict(type='str', required=True, no_log=True),
            username=dict(type='str', required=False),
            newname=dict(type='str', required=False),
            newusername=dict(type='str', required=False),
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
    newname = module.params['newname']
    newusername = module.params['newusername']
    uri = module.params['uri']
    description = module.params['description']
    encrypt_description = module.params['encrypt_description']
    verify = module.params['verify']
    fingerprint = module.params['fingerprint']

    Passbolt = passbolt(apiurl=passbolt_uri, privatekey=gpgkey, passphrase=passphrase, fingerprint=fingerprint,
                        verify=verify)

    response = Passbolt.updatepassword(name, password, username, newname, newusername, uri, description, encrypt_description)
    if response == "The resource has been updated successfully.":
        changed = True
        module.exit_json(msg=response, changed=changed)
    else:
        changed = False
        module.fail_json(msg=response)


if __name__ == '__main__':
    main()
