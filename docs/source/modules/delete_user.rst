.. _delete_user_module:


delete_user -- delete user in Passbolt
======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt delete user module deletes a user in Passbolt via the API.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN)


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  username (True, str, None)
    The email address of the user you wish to delete.









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Delete User
      daniel_lynch.passbolt.delete_user:
        passbolt_uri: "https://passbolt.example.com"
        gpgkey: "{{ gpgkey }}"
        passphrase: "password"
        username: "testing@example.com"
      delegate_to: localhost





Status
------





Authors
~~~~~~~

- Daniel Lynch (@daniel-lynch)

