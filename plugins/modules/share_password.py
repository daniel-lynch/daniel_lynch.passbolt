#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2023, Daniel Lynch <daniel.lynch2016@gmail.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
module: share_password
short_description: Share password in Passbolt.
description:
    - The Passbolt Share password module shares a password with Users and/or Groups in Passbolt via the API.
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
      - The name of the password you wish to share.
  users:
    type: list
    elements: str
    required: false
    description:
      - The list of users you wish to share the password with. (Required unless groups list is provided.)
  groups:
    type: list
    elements: str
    required: false
    description:
      - The list of groups you wish to share the password with. (Required unless users list is provided.)
  permission:
    type: str
    required: false
    description:
      - The permission level you wish to grant. Must be one of the following; Read, Update, or Owner. (Defaults to Read.)
    default: Read
  username:
    type: str
    required: false
    description:
      - The username field of the password you wish to create. (Optional but strongly encouraged.)
"""

EXAMPLES = """
- name: Share Password
  daniel_lynch.passbolt.share_password:
    passbolt_uri: "https://passbolt.example.com"
    gpgkey: "{{ gpgkey }}"
    passphrase: "password"
    name: "Testing"
    users:
      - daniel.lynch2016@gmail.com
    groups:
      - Users
    permission: Read
    username: "Test"
  delegate_to: localhost

- name: Share Password Using Fingerprint
  daniel_lynch.passbolt.share_password:
    passbolt_uri: "https://passbolt.example.com"
    fingerprint="{{ fingerprint }}"
    name: "Testing"
    users:
      - daniel.lynch2016@gmail.com
    groups:
      - Users
    permission: Read
    username: "Test"
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
            users=dict(type='list', elements='str', required=False),
            groups=dict(type='list', elements='str', required=False),
            permission=dict(type='str', required=False, default='Read'),
            username=dict(type='str', required=False),
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
    users = module.params['users']
    groups = module.params['groups']
    permission = module.params['permission']
    username = module.params['username']
    verify = module.params['verify']
    fingerprint = module.params['fingerprint']

    Passbolt = passbolt(apiurl=passbolt_uri, privatekey=gpgkey, passphrase=passphrase, fingerprint=fingerprint,
                        verify=verify)

    response = Passbolt.sharepassword(name, username, users, groups, permission)
    if response == "The operation was successful.":
        changed = True
        module.exit_json(msg=response, changed=changed)
    else:
        changed = False
        module.fail_json(msg=response)


if __name__ == '__main__':
    main()
