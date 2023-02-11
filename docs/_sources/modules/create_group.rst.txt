.. _create_group_module:


create_group -- Create group in Passbolt
========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt create group module creates a group in Passbolt via the API.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN)


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  name (True, str, None)
    The name of the group you wish to create.


  admins (True, list, None)
    A list of group admins.


  users (False, list, None)
    A list of group users.









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create Group
      daniel_lynch.passbolt.create_group:
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

