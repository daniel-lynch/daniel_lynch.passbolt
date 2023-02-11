#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2023, Daniel Lynch <daniel.lynch2016@gmail.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
module: delete_group
short_description: Delete group in Passbolt
description:
    - The Passbolt delete group module deletes a group in Passbolt via the API.
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
      - The name of the group you wish to delete.
"""

EXAMPLES = """
- name: Delete Group
  daniel_lynch.passbolt.delete_group:
    passbolt_uri: "https://passbolt.example.com"
    gpgkey: "{{ gpgkey }}"
    passphrase: "password"
    name: "Users"
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
            gpgkey=dict(type='str', required=True, no_log=True),
            passphrase=dict(type='str', required=True, no_log=True),
            name=dict(type='str', required=True)
        ),
        supports_check_mode=True,
    )

    if not HAS_ANOTHER_LIBRARY:
        module.fail_json(msg="missing lib", exception=ANOTHER_LIBRARY_IMPORT_ERROR)

    passbolt_uri = module.params['passbolt_uri']
    gpgkey = module.params['gpgkey']
    passphrase = module.params['passphrase']
    name = module.params['name']

    Passbolt = passbolt(gpgkey, passphrase, passbolt_uri)

    response = Passbolt.deletegroup(name)
    if response == "The group was deleted successfully.":
        changed = True
        module.exit_json(msg=response, changed=changed)
    else:
        changed = False
        module.fail_json(msg=response)


if __name__ == '__main__':
    main()
