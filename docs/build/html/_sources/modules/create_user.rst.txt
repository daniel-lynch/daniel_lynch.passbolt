.. _create_user_module:


create_user -- Create user in Passbolt
======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt create user module creates a user in Passbolt via the API.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN)


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  username (True, str, None)
    The email address of the user you wish to create.


  firstname (True, str, None)
    The first name of the user you wish to create.


  lastname (True, str, None)
    The last name of the user you wish to create.


  admin (False, bool, False)
    Grant the user admin privileges (Defaults false)









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create User
      daniel_lynch.passbolt.create_user:
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

