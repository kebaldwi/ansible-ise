#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: guest_user_info
short_description: Information module for Guest User
description:
- Get all Guest User.
- Get Guest User by id.
- Get Guest User by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
  sortasc:
    description:
    - Sortasc query parameter. Sort asc.
    type: str
  sortdec:
    description:
    - Sortdec query parameter. Sort desc.
    type: str
  filter:
    description:
    - >
      Filter query parameter. <br/> **Simple filtering** should be available through the filter query string
      parameter. The structure of a filter is a triplet of field operator and value separated with dots. More than
      one filter can be sent. The logical operator common to ALL filter criteria will be by default AND, and can
      be changed by using the "filterType=or" query string parameter. Each resource Data model description should
      specify if an attribute is a filtered field. <br/> Operator | Description <br/>
      ------------|----------------- <br/> EQ | Equals <br/> NEQ | Not Equals <br/> GT | Greater Than <br/> LT |
      Less Then <br/> STARTSW | Starts With <br/> NSTARTSW | Not Starts With <br/> ENDSW | Ends With <br/> NENDSW
      | Not Ends With <br/> CONTAINS | Contains <br/> NCONTAINS | Not Contains <br/>.
    type: list
  filterType:
    description:
    - >
      FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and
      can be changed by using the parameter.
    type: str
  id:
    description:
    - Id path parameter.
    type: str
  name:
    description:
    - Name path parameter.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.guest_user
# Reference by Internet resource
- name: Guest User reference
  description: Complete reference of the Guest User object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Guest User
  cisco.ise.guest_user_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
    sortasc: asc
    sortdec: string
    filter: []
    filterType: AND
  register: result

- name: Get Guest User by id
  cisco.ise.guest_user_info:
    id: string
  register: result

- name: Get Guest User by name
  cisco.ise.guest_user_info:
    name: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "GuestUser": {
        "id": "string",
        "name": "string",
        "guestType": "string",
        "status": "string",
        "sponsorUserName": "string",
        "sponsorUserId": "string",
        "guestInfo": {
          "userName": "string",
          "password": "string",
          "creationTime": "string",
          "enabled": true,
          "notificationLanguage": "string"
        },
        "guestAccessInfo": {
          "validDays": 0,
          "fromDate": "string",
          "toDate": "string",
          "location": "string"
        },
        "customFields": {},
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    }
"""
