# containernerds.discord
[![CI](https://github.com/ContainerNerds/containernerds.discord/actions/workflows/ansible-test.yml/badge.svg?branch=main)](https://github.com/ContainerNerds/containernerds.discord/actions/workflows/ansible-test.yml)


Ansible Collection to allow communication to Discord from Ansible.

# Installation
`ansible-galaxy collection install containernerds.discord`


# Usage
```yml
---
- hosts: localhost
  tasks:
    - name: Send Discord Message
      containernerds.discord.webhook_message:
        msg: "Intergration Test"
        webhook: "Discord Webhook https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks"
```

### With embed
```yml
- hosts: localhost
  tasks:
  - name: Send Discord Message Embed
    containernerds.discord.webhook_message:
      msg: "containernerds.discord Automated Integration Test With Embed"
      webhook: "{{ webhook }}"
      embeds: [{
        "author": {
          "name": "Container Nerds",
          "url": "http://containernerds.com",
          "icon_url": "https://avatars.githubusercontent.com/u/45960414?s=200&v=4"
        },
        "title": "Consult with us",
        "url": "http://containernerds.com",
        "description": "Enterprise Cloud Architect Consulting Group",
        "color": 1862655,
        "fields": [
          {
            "name": "Python Version",
            "value": "Python {{ ansible_python_version }}",
            "inline": True
          },
          {
            "name": "Ansible Version",
            "value": "Ansible {{ ansible_version.full }}",
            "inline": True
          }
        ],
        "thumbnail": {
          "url": "https://avatars.githubusercontent.com/u/45960414?s=200&v=4"
        },
        "image": {
          "url": "https://avatars.githubusercontent.com/u/45960414?s=200&v=4"
        },
        "footer": {
          "text": "© 2021 Container Nerds",
          "icon_url": "https://avatars.githubusercontent.com/u/45960414?s=200&v=4"
        }
      }]
    delegate_to: localhost
```
Additional Embed objects can be found here https://discord.com/developers/docs/resources/channel#embed-object
