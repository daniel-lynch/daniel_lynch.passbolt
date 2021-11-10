.. _update_group_module:


update_group -- Update group in Passbolt
========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt update group module updates a group in Passbolt via the API. Currently only supports adding Users and Admins due to API limitations.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN)


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  name (True, str, None)
    The name of the group you wish to update.


  admins (False, list, None)
    A list of admins to add to the group.


  users (False, list, None)
    A list of users to add to the group.









Examples
--------

.. code-block:: yaml+jinja

    
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





Status
------





Authors
~~~~~~~

- Daniel Lynch (@daniel-lynch)

