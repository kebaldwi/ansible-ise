#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: endpoint_group
short_description: Resource module for Endpoint Group
description:
- Manage operations create, update, delete of the resource Endpoint Group.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    description:
      description: Endpoint Group's description.
      type: str
    id:
      description: Endpoint Group's id.
      type: str
    name:
      description: Endpoint Group's name.
      type: str
    systemDefined:
      description: SystemDefined flag.
      type: bool
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.endpoint_group
# Reference by Internet resource
- name: Endpoint Group reference
  description: Complete reference of the Endpoint Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.endpoint_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: Description
    name: MyEndpointGroup
- name: Update by id
  cisco.ise.endpoint_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: 'Identity Group for Profile: Cisco-Meraki-Device'
    id: 1e2700a0-8c00-11e6-996c-525400b48521
    name: Cisco-Meraki-Device
    systemDefined: true
- name: Delete by id
  cisco.ise.endpoint_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
- name: Ise request doc
  cisco.ise.endpoint_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {}
  - {}
  - {}
  - 
"""
