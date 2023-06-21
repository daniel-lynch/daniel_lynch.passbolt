#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2023, Daniel Lynch <daniel.lynch2016@gmail.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
module: update_user
short_description: Update user in Passbolt
description:
    - The Passbolt update user module updates a user in Passbolt via the API.
    - You either need the gpgkey and the passphrase or the fingerprint of the secret key stored in the gpg-agent.
author: "Daniel Lynch (@daniel-lynch)"
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
  username:
    type: str
    required: true
    description:
      - The email address of the user you wish to update.
  firstname:
    type: str
    required: true
    description:
      - The new first name of the user you wish to update.
  lastname:
    type: str
    required: true
    description:
      - The new last name of the user you wish to update.
  admin:
    type: bool
    required: false
    description:
      - Grant the user admin privileges (Defaults false)
    default: false
"""

EXAMPLES = """
- name: Update User
  daniel_lynch.passbolt.update_user:
    passbolt_uri: "https://passbolt.example.com"
    gpgkey: "{{ gpgkey }}"
    passphrase: "password"
    username: "testing@example.com"
    firstname: "Test"
    lastname: "Ing"
    admin: True
  delegate_to: localhost

- name: Update User Using Fingerprint
  daniel_lynch.passbolt.update_user:
    passbolt_uri: "https://passbolt.example.com"
    fingerprint="{{ fingerprint }}"
    username: "testing@example.com"
    firstname: "Test"
    lastname: "Ing"
    admin: True
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
            username=dict(type='str', required=True),
            firstname=dict(type='str', required=True),
            lastname=dict(type='str', required=True),
            admin=dict(type='bool', required=False, default=False),
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
    username = module.params['username']
    firstname = module.params['firstname']
    lastname = module.params['lastname']
    admin = module.params['admin']
    verify = module.params['verify']
    fingerprint = module.params['fingerprint']

    Passbolt = passbolt(apiurl=passbolt_uri, privatekey=gpgkey, passphrase=passphrase, fingerprint=fingerprint,
                        verify=verify)

    response = Passbolt.updateuser(username, firstname, lastname, admin)
    if response == "The user has been updated successfully.":
        changed = True
        module.exit_json(msg=response, changed=changed)
    else:
        changed = False
        module.fail_json(msg=response)


if __name__ == '__main__':
    main()
