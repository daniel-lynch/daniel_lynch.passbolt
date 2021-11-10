.. _delete_password_module:


delete_password -- Delete password in Passbolt.
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt delete password module deletes a password in Passbolt via the API.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN).


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  name (True, str, None)
    The name of the password you wish to delete.


  username (False, str, None)
    The username field of the password you wish to delete. (Optional but strongly encouraged if there are multiple passwords with the same name.)









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Delete Password
      daniel_lynch.passbolt.delete_password:
        passbolt_uri: "https://passbolt.example.com"
        gpgkey: "{{ gpgkey }}"
        passphrase: "password"
        name: "Testing"
        username: "Test"
      delegate_to: localhost





Status
------





Authors
~~~~~~~

- Daniel Lynch (@daniel-lynch)

