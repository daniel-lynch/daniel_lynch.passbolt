#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2023, Daniel Lynch <daniel.lynch2016@gmail.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
module: update_group
short_description: Update group in Passbolt
description:
    - The Passbolt update group module updates a group in Passbolt via the API. Currently only supports adding Users and Admins due to API limitations.
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
  name:
    type: str
    required: true
    description:
      - The name of the group you wish to update.
  admins:
    type: list
    elements: str
    required: false
    description:
      - A list of admins to add to the group.
  users:
    type: list
    elements: str
    required: false
    description:
      - A list of users to add to the group.
"""

EXAMPLES = """
- name: Update Group
  daniel_lynch.passbolt.update_group:
    passbolt_uri: "https://passbolt.example.com"
    gpgkey: "{{ gpgkey }}"
    passphrase: "password"
    name: "Users"
    admins:
      - testing@example.com
    users:
      - testing2@example.com
  delegate_to: localhost

- name: Update Group Using Fingerprint
  daniel_lynch.passbolt.update_group:
    passbolt_uri: "https://passbolt.example.com"
    fingerprint="{{ fingerprint }}"
    name: "Users"
    admins:
      - testing@example.com
    users:
      - testing2@example.com
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
            admins=dict(type='list', elements='str', required=False),
            users=dict(type='list', elements='str', required=False),
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
    admins = module.params['admins']
    users = module.params['users']
    verify = module.params['verify']
    fingerprint = module.params['fingerprint']
    Passbolt = passbolt(apiurl=passbolt_uri, privatekey=gpgkey, passphrase=passphrase, fingerprint=fingerprint,
                        verify=verify)


    response = Passbolt.updategroup(name, admins, users)
    if response == "The operation was successful.":
        changed = True
        module.exit_json(msg=response, changed=changed)
    else:
        changed = False
        module.fail_json(msg=response)


if __name__ == '__main__':
    main()
