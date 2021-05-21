#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: filter_policy
short_description: Resource module for Filter Policy
description:
- Manage operations create, update, delete of the resource Filter Policy.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    domains:
      description: Filter Policy's domains.
      type: str
    id:
      description: Id path parameter.
      type: string
    sgt:
      description: Filter Policy's sgt.
      type: str
    subnet:
      description: Filter Policy's subnet.
      type: str
    vn:
      description: Filter Policy's vn.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.filter_policy
# Reference by Internet resource
- name: Filter Policy reference
  description: Complete reference of the Filter Policy object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.filter_policy:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    domains: Sxp Vpn Name
    sgt: sgt
    subnet: subnetAddress
    vn: virtualNetwork
- name: Update by id
  cisco.ise.filter_policy:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    domains: Sxp Vpn Name
    id: string
    sgt: sgt
    subnet: subnetAddress
    vn: virtualNetwork
- name: Delete by id
  cisco.ise.filter_policy:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
- name: Ise request doc
  cisco.ise.filter_policy:
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
