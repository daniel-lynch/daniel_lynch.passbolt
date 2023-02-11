[![CI](https://github.com/daniel-lynch/daniel_lynch.passbolt/actions/workflows/ansible-test.yml/badge.svg?branch=main)](https://github.com/daniel-lynch/daniel_lynch.passbolt/actions/workflows/ansible-test.yml)
# Readme
Ansible Collection to allow Passbolt managment from Ansible.

## Requirements
Python3.6+ https://www.python.org/downloads/

GnuPG https://gnupg.org/download/index.html

Passbolt python module `pip install passbolt`



## Install:
`ansible-galaxy collection install daniel_lynch.passbolt`

## Examples

### Get Password. [Docs](docs/source/lookup/get_password.rst)
```yaml
---
- hosts: localhost
  vars:
    passbolt_uri: https://passbolt.djlynch.us
    gpgkey: "{{ lookup('file', 'key.asc') }}"
    passphrase: Password
  tasks:
    - debug:
        msg: "{{ lookup('daniel_lynch.passbolt.get_password', 'Testing', gpgkey=gpgkey, passphrase=passphrase, passbolt_uri=passbolt_uri) }}"
```

### Create User. [Docs](docs/source/modules/create_user.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Create User
      daniel_lynch.passbolt.create_user:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        username: "testing@example.com"
        firstname: "Test"
        lastname: "Ing"
        admin: True
```

### Update User. [Docs](docs/source/modules/update_user.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Update User
      daniel_lynch.passbolt.update_user:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        username: "testing@example.com"
        firstname: "Test"
        lastname: "Ing"
        admin: True
```

### Delete User. [Docs](docs/source/modules/delete_user.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Delete User
      daniel_lynch.passbolt.delete_user:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        username: "testing@example.com"
```

### Create Group. [Docs](docs/source/modules/create_group.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Create Group
      daniel_lynch.passbolt.create_group:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        name: "Test"
        admins:
        - "{{ admin }}"
        users:
        - "{{ user }}"
```

### Update Group. [Docs](docs/source/modules/update_group.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Update Group
      daniel_lynch.passbolt.update_group:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        name: "Test"
        admins:
        - "{{ admin2 }}"
        users:
        - "{{ user2 }}"
```

### Delete Group. [Docs](docs/source/modules/delete_group.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Delete Group
      daniel_lynch.passbolt.delete_group:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        name: "Test"
```

### Create Password. [Docs](docs/source/modules/create_password.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Create Password
      daniel_lynch.passbolt.create_password:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        name: "Testing"
        password: "password"
        username: "Test"
        uri: "test.com"
        description: "This is a description"
```

### Update Password. [Docs](docs/source/modules/update_password.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Update Password
      daniel_lynch.passbolt.update_password:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        name: "Testing"
        password: "password"
        username: "Test"
        newname: "Testing2"
        newusername: "Test2"
        uri: "test2.com"
        description: "This is a description2"
```

### Share Password. [Docs](docs/source/modules/share_password.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Share Password
      daniel_lynch.passbolt.share_password:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        name: "Testing"
        users:
        - "{{ admin2 }}"
        groups:
        - Users
        permission: Read
        username: "Test"
```

### Delete Password. [Docs](docs/source/modules/delete_password.rst)
```yaml
---
- hosts: localhost
  tasks:
    - name: Delete Password
      daniel_lynch.passbolt.delete_password:
        passbolt_uri: "{{ passbolt_uri }}"
        gpgkey: "{{ gpgkey }}"
        passphrase: "{{ passphrase }}"
        name: "Testing"
        username: "Test"
```

## Considerations
Use ansible-vault to encrypt passphrase and GPG key https://docs.ansible.com/ansible/2.8/user_guide/playbooks_vault.html#single-encrypted-variable
