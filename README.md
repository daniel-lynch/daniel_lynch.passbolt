# Readme
Ansible Collection to allow Passbolt managment from Ansible.

## Install:
`ansible-galaxy collection install daniel_lynch.passbolt`

## Examples

### Create User. [Docs](docs/build/html/modules/create_user.html)
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

### Update User. [Docs](docs/build/html/modules/update_user.html)
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

### Delete User. [Docs](docs/build/html/modules/delete_user.html)
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

### Create Group. [Docs](docs/build/html/modules/create_group.html)
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

### Update Group. [Docs](docs/build/html/modules/update_group.html)
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

### Delete Group. [Docs](docs/build/html/modules/delete_group.html)
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

### Create Password. [Docs](docs/build/html/modules/create_password.html)
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

### Update Password. [Docs](docs/build/html/modules/update_password.html)
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

### Share Password. [Docs](docs/build/html/modules/share_password.html)
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

### Delete Password. [Docs](docs/build/html/modules/delete_password.html)
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
