.. _share_password_module:


share_password -- Share password in Passbolt.
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Passbolt Share password module shares a password with Users and/or Groups in Passbolt via the API.






Parameters
----------

  passbolt_uri (True, str, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN).


  gpgkey (True, str, None)
    The GPG Private key used to access Passbolt.


  passphrase (True, str, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  name (True, str, None)
    The name of the password you wish to share.


  users (False, list, None)
    The list of users you wish to share the password with. (Required unless groups list is provided.)


  groups (False, list, None)
    The list of groups you wish to share the password with. (Required unless users list is provided.)


  permission (False, str, Read)
    The permission level you wish to grant. Must be one of the following; Read, Update, or Owner. (Defaults to Read.)


  username (False, str, None)
    The username field of the password you wish to create. (Optional but strongly encouraged.)









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Share Password
      daniel_lynch.passbolt.share_password:
        passbolt_uri: "https://passbolt.example.com"
        gpgkey: "{{ gpgkey }}"
        passphrase: "password"
        name: "Testing"
        users:
          - daniel.lynch2016@gmail.com
        groups:
          - Users
        permission: Read
        username: "Test"
      delegate_to: localhost





Status
------





Authors
~~~~~~~

- Daniel Lynch (@daniel-lynch)

