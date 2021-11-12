.. _get_password_module:


get_password -- Get password from Passbolt
==========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

This lookup returns a list of passwords from Passbolt.






Parameters
----------

  name (True, any, None)
    The name of the password in passbolt.


  username (False, any, None)
    The username field of the password. Use this to narrow down your search if there are multiple passwords with the same name.


  passbolt_uri (True, any, None)
    The Passbolt instance Fully Qualified Domain Name(FQDN)


  passphrase (True, any, None)
    The Passphrase used with the GPG Private key used to access Passbolt.


  gpgkey (True, any, None)
    The GPG Private key used to access Passbolt.


  return_format (optional, any, password)
    Controls how passwords are returned.

    ``dict`` returns a list of dictionaries that includes the password name, username, uri, description,

    ``password`` returns a list of just the passwords









Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get list of passwords with the name Testing
      ansible.builtin.debug:
        msg: "{{ lookup('daniel_lynch.passbolt.get_password', 'Testing', gpgkey=gpgkey, passphrase=passphrase, passbolt_uri=passbolt_uri) }}"
    - name: Get list of passwords with the name Testing and username Test
      ansible.builtin.debug:
        msg: "{{ lookup('daniel_lynch.passbolt.get_password', 'Testing', username='Test', gpgkey=gpgkey, passphrase=passphrase, passbolt_uri=passbolt_uri) }}"
    - name: Get list of password dictionaries with the name Testing
      ansible.builtin.debug:
        msg: "{{ lookup('daniel_lynch.passbolt.get_password', 'Testing', return_format='dict', gpgkey=gpgkey, passphrase=passphrase, passbolt_uri=passbolt_uri) }}"





Status
------





Authors
~~~~~~~

- Daniel Lynch <daniel.lynch2016@gmail.com>

