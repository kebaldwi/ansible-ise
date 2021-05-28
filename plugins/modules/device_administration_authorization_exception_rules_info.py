#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_administration_authorization_exception_rules_info
short_description: Information module for Device Administration Authorization Exception Rules
description:
- Get all Device Administration Authorization Exception Rules.
- Get Device Administration Authorization Exception Rules by id.
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
- module: cisco.ise.plugins.module_utils.definitions.device_administration_authorization_exception_rules
# Reference by Internet resource
- name: Device Administration Authorization Exception Rules reference
  description: Complete reference of the Device Administration Authorization Exception Rules object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Device Administration Authorization Exception Rules
  cisco.ise.device_administration_authorization_exception_rules_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    policyId: string
  register: result

- name: Get Device Administration Authorization Exception Rules by id
  cisco.ise.device_administration_authorization_exception_rules_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    policyId: string
    id: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "rule": {
        "id": "string",
        "name": "string",
        "description": "string",
        "hitCounts": 0,
        "rank": 0,
        "state": "string",
        "default": true,
        "condition": {
          "conditionType": "string",
          "isNegate": true,
          "name": "string",
          "id": "string",
          "description": "string",
          "dictionaryName": "string",
          "attributeName": "string",
          "attributeId": "string",
          "operator": "string",
          "dictionaryValue": "string",
          "attributeValue": "string",
          "children": [
            {
              "conditionType": "string",
              "isNegate": true
            }
          ],
          "hoursRange": {
            "startTime": "string",
            "endTime": "string"
          },
          "hoursRangeException": {
            "startTime": "string",
            "endTime": "string"
          },
          "weekDays": [
            "string"
          ],
          "weekDaysException": [
            "string"
          ],
          "datesRange": {
            "startDate": "string",
            "endDate": "string"
          },
          "datesRangeException": {
            "startDate": "string",
            "endDate": "string"
          }
        }
      },
      "commands": [
        "string"
      ],
      "profile": "string"
    }
"""
