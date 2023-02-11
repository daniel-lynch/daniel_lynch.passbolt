.. _delete_group_module:


delete_group -- Delete group in Passbolt
========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt delete group module deletes a group in Passbolt via the API.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN)


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  name (True, str, None)
    The name of the group you wish to delete.









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Delete Group
      daniel_lynch.passbolt.delete_group:
        passbolt_uri: "https://passbolt.example.com"
        gpgkey: "{{ gpgkey }}"
        passphrase: "password"
        name: "Users"
      delegate_to: localhost





Status
------





Authors
~~~~~~~

- Daniel Lynch (@daniel-lynch)

