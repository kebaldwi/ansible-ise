#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_access_authorization_rules_info
short_description: Information module for Network Access Authorization Rules
description:
- Get all Network Access Authorization Rules.
- Get Network Access Authorization Rules by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  policyId:
    description:
    - PolicyId path parameter. Policy id.
    type: str
  id:
    description:
    - Id path parameter. Rule id.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_authorization_rules
# Reference by Internet resource
- name: Network Access Authorization Rules reference
  description: Complete reference of the Network Access Authorization Rules object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Access Authorization Rules
  cisco.ise.network_access_authorization_rules_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    policyId: string
  register: result
- name: Get Network Access Authorization Rules by id
  cisco.ise.network_access_authorization_rules_info
    policyId: string
    id: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'rule': {'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}}, 'profile': ['string'], 'securityGroup': 'string'}
  - [{'rule': {'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True}}, 'profile': ['string'], 'securityGroup': 'string'}]
"""
