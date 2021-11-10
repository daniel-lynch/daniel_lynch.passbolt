.. _create_password_module:


create_password -- Create password in Passbolt
==============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt create password module creates a password in Passbolt via the API.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN)


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  name (True, str, None)
    The name of the password you wish to create.


  password (True, str, None)
    The password you wish to create.


  username (False, str, None)
    The username field of the password you wish to create. (Optional but strongly encouraged.)


  uri (False, str, None)
    The uri field of the password you wish to create. (Optional)


  description (False, str, None)
    The description field of the password you wish to create. (Optional)


  encrypt_description (False, bool, True)
    Option to create the password description as a secret and encrypt it in the database. (Optional. Defaults to true.)









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create Password
      daniel_lynch.passbolt.create_password:
        passbolt_uri: "https://passbolt.example.com"
        gpgkey: "{{ gpgkey }}"
        passphrase: "password"
        name: "Testing"
        password: "password"
        username: "Test"
        uri: "test.com"
        description: "This is a description"
      delegate_to: localhost





Status
------





Authors
~~~~~~~

- Daniel Lynch (@daniel-lynch)

