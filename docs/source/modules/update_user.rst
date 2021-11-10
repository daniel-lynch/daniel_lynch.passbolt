.. _update_user_module:


update_user -- Update user in Passbolt
======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt update user module updates a user in Passbolt via the API.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN)


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  username (True, str, None)
    The email address of the user you wish to update.


  firstname (True, str, None)
    The new first name of the user you wish to update.


  lastname (True, str, None)
    The new last name of the user you wish to update.


  admin (False, bool, False)
    Grant the user admin privileges (Defaults false)









Examples
--------

.. code-block:: yaml+jinja

    
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





Status
------





Authors
~~~~~~~

- Daniel Lynch (@daniel-lynch)

