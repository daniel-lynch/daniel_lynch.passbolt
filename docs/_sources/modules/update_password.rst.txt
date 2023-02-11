.. _update_password_module:


update_password -- Update password in Passbolt.
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt update password module updates a password in Passbolt via the API.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN).


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  name (True, str, None)
    The name of the password you wish to update.


  password (True, str, None)
    The updated password.


  username (False, str, None)
    The username field of the password you wish to update. (Optional but strongly encouraged if there are multiple passwords with the same name.)


  newname (False, str, None)
    The new name of the password you wish to update. (Optional)


  newusername (False, str, None)
    The new username of the password you wish to update. (Optional)


  uri (False, str, None)
    The uri field of the password you wish to update. (Optional)


  description (False, str, None)
    The description field of the password you wish to update. (Optional)


  encrypt_description (False, bool, True)
    Option to create the password description as a secret and encrypt it in the database. (Optional. Defaults to true.)









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Update Password
      daniel_lynch.passbolt.update_password:
        passbolt_uri: "https://passbolt.example.com"
        gpgkey: "{{ gpgkey }}"
        passphrase: "password"
        name: "Testing"
        password: "password"
        username: "Test"
        newname: "Testing2"
        newusername: "Test2"
        uri: "test2.com"
        description: "This is a description2"
      delegate_to: localhost





Status
------





Authors
~~~~~~~

- Daniel Lynch (@daniel-lynch)

