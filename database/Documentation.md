# Table of contents
- [1. Introduction](#1-introduction)
  * [1.1 Purpose](#11-purpose)
  * [1.2 Usage](#12-usage)
  * [1.3 Framework and deployment strategy](#13-framework-and-deployment-strategy)
- [2. API](#2-api)
  * [2.1 GET-calls](#21-get-calls)
  * [2.1 GET-calls](#21-get-calls)
    + [2.1.1 All entries of one type](#211-all-entries-of-one-type)
    + [2.1.2 Single entry by unique identifier](#212-single-entry-by-unique-identifier)
    + [2.1.3 Ping targets](#213-ping-targets)
    + [2.1.4 Dates by different categories](#214-dates-by-different-categories)
    + [2.1.5 Entry by non-unique identifier](#215-entry-by-non-unique-identifier)
  * [2.1 POST-calls](#22-post-calls)
  * [2.1 PATCH-calls](#23-patch-calls)
- [3. Web Frontend](#3-web-frontend)
  * [3.1 Home](#31-home)
  * [3.2 Creating dates](#32-creating-dates)
  * [3.3 Viewing and managing dates](#33-viewing-and-managing-dates)
  * [3.4 Managing properties (Subjects, User, Roles, etc.)](#34-managing-properties-subjects-user-roles-etc))
- [4. Discord Bot](#4-discord-bot)
  * [4.1 Deployment](#41-deployment)
  * [4.2 Usage](#42-usage)
    + [4.2.1 Commands](#421-commands)
    + [4.2.2 Customization](#422-customization)
    + [4.2.3 Permissions](#423-permissions)

# 1. Introduction
## 1.1 Purpose
## 1.2 Usage
## 1.3 Framework and deployment strategy

# 2. API
## 2.1 Objects
### 2.1.1 Date
Example Object:
<details>
  <summary>Click to expand!</summary>
  
  ```json
    {
        "id": 1,
        "gid": "only_lower_case_ascii_id",
        "title": "Example Title",
        "subtitle": "Example Subtitle",
        "subject": {
            "name": "Example Subject",
            "exam_ects": 5.0,
            "prac_ects": 2.5,
            "exam_description": "Full description of the exam - As much info as possible",
            "prac_description": "Full description of the 'Übungen' - As much info as possible",
            "studon_url": "someStudonURL.com",
            "zoom_url": "someZoomURL.com",
            "contact": "Contact info of the professor/teacher",
            "further_info": "Any information not specific to the exam ot practice",
            "ping_tag": "@somepingtag123",
            "color": "#ffffff"
        },
        "description": "Full description of the date (e.g. requirements)",
        "due_date": "01/01/21",
        "due_time": "13:00",
        "repeat": {
            "id": 1,
            "display_name": "Daily"
        },
        "create_date": "01/01/21",
        "create_time": "13:00",
        "creator": {
            "id": 1,
            "login_name": "LoginName",
            "password": "123456",
            "discord_user": {
                "id": "@bsca21398c1123",
                "name": "Name",
                "color": "#ff0000",
                "studon": "ab01cdef"
            }
        },
        "expired": 0,
        "ping_roles": [
            {
                "id": "@scad123hjdj1",
                "name": "RoleName",
                "color": "#ffffff"
            }
        ],
        "ping_users": [
            {
                "id": "@bsca21398c1123",
                "name": "Name",
                "color": "#ff0000",
                "studon": "ab01cdef"
            },
            {
                "id": "@hjidcs89123",
                "name": "Name2",
                "color": "#ff0000",
                "studon": "cd10abcd"
            }
        ]
    }
  ```
</details>

### 2.1.2 Subject
### 2.1.3 Role
### 2.1.4 User
### 2.1.5 Creator
### 2.1.6 Repeat
## 2.2 GET-calls
### 2.2.1 All entries of one type
#### Dates
Call: `/dates`  
Example Output: 
#### Not yet expired dates
`/dates`
#### Expired dates
`/dates`
#### Users
`/dates`
#### Roles
`/dates`
#### Subjects
`/dates`
#### Repeats
`/dates`
#### Creators
`/dates`
### 2.2.2 Single entry by unique identifier
### 2.2.3 Ping targets
### 2.2.4 Dates by different categories
### 2.2.5 Entry by non-unique identifier
## 2.3 POST-calls
## 2.4 PATCH-calls

# 3. Web Frontend
## 3.1 Home
## 3.2 Creating dates
## 3.3 Viewing and managing dates
## 3.4 Managing properties (Subjects, User, Roles, etc.)

# 4. Discord Bot
## 4.1 Deployment
## 4.2 Usage
### 4.2.1 Commands
### 4.2.2 Customization
### 4.2.3 Permissions
