#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2021, Daniel Lynch <daniel.lynch2016@gmail.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
module: create_password
short_description: Create password in Passbolt
description:
    - The Passbolt create password module creates a password in Passbolt via the API.
author: "Daniel Lynch (@daniel-lynch)"
options:
  passbolt_uri:
    type: str
    required: true
    description:
      - The Passbolt instance Fully Qualified Domain Name(FQDN)
  gpgkey:
    type: str
    required: true
    description:
      - The GPG Private key used to access Passbolt.
  passphrase:
    type: str
    required: true
    description:
      - The Passphrase used with the GPG Private key used to access Passbolt.
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
- name: Create Password
  daniel_lynch.passbolt.create_password:
    passbolt_uri: "https://passbolt.example.com"
    gpgkey: "{{ gpgkey }}"
    passphrase: "password"
    name: "Testing"
    password: "password"
    username: "Test"
    uri: "test.com"
    description: "This is a description"
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


def main():
    module = AnsibleModule(
        argument_spec=dict(
            passbolt_uri=dict(type='str', required=True, no_log=True),
            gpgkey=dict(type='str', required=True, no_log=True),
            passphrase=dict(type='str', required=True, no_log=True),
            name=dict(type='str', required=True),
            password=dict(type='str', required=True, no_log=True),
            username=dict(type='str', required=False),
            uri=dict(type='str', required=False),
            description=dict(type='str', required=False),
            encrypt_description=dict(type='bool', required=False, default=True)
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

    Passbolt = passbolt(gpgkey, passphrase, passbolt_uri)

    response = Passbolt.createpassword(name, password, username, uri, description, encrypt_description)
    if response == "The resource has been added successfully.":
        changed = True
        module.exit_json(msg=response, changed=changed)
    else:
        changed = False
        module.fail_json(msg=response)


if __name__ == '__main__':
    main()
