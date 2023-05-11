# Cisco DNA Center open-source integrations with GitHub and GitLab

This repo is for two open-source integrations that will update and maintain in sync Cisco DNA Center Projects and CLI templates with GitHub and GitLab Repos hosting the templates files.
The Repos will be used as a single source of truth for all desired settings, templates and profiles, providing consistent configurations across multiple Cisco DNA Center Clusters, lab and production.

**Cisco Products & Services:**

- Cisco DNA Center, devices managed by Cisco DNA Center
- Cisco DNA Center Python SDK

**Tools & Frameworks:**

- Python environment to run the application
- GitHub and GitLab accounts, private token and repos
- Optional: CI/CD platform if desired to automate the process

**Usage**

Usage details for each integration are provided in the README.md files from the folder of the integration.

Sample Output **GitHub Sync**:

```shell
# Cisco DNA Center
DNAC_URL = 'https://dnacenter'
DNAC_USER = 'user'
DNAC_PASS = 'password'
DNAC_PROJECT = 'Cisco DNA Center Project'

# GitHub
GITHUB_TOKEN = 'token'   # GitHub access token
GITHUB_USERNAME = 'user'
GITHUB_REPO = 'repo'
```

Sample Output:

```shell
python dnacenter_github_sync.py

INFO:root: App "dnacenter_github_sync.py" Start, 2023-04-03 19:32:42
INFO:root: Repo "dnacenter_github_templates" found!
INFO:root: Repo "dnacenter_github_templates" files:
INFO:root: File: aaa_config.txt
INFO:root: File: csr_logging.txt
INFO:root: File: snmp_ntp.txt
INFO:root: Collected all commit comments for "dnacenter_github_templates" repo
INFO:root: Project "GitHub_Project" id: bf74f896-b002-49b1-...
INFO:root: Template name: aaa_config
INFO:root: Template content:
{#
This template has been pulled from GitHub.
Uploaded to Cisco DNA Center by GitHub_Sync App
Author: gzapodea@cisco.com
Date: 2023-03-24T21:19:42Z
Commit message: updated templates, new template
Commit URL: https://github.com/zapodeanu/dnacenter_github_templates/commit/50724c24f7f7ebe435ba...
Commit Diff: @@ -0,0 +1,5 @@
+!
+aaa new-model
+aaa authentication login default local
+aaa authorization exec default local
+!
\ No newline at end of file
#}
!
!
aaa new-model
aaa authentication login default local
aaa authorization exec default local
!
INFO:root: Template "aaa_config" has not changed, identical template on Cisco DNA Center
INFO:root: Template name: csr_logging
INFO:root: Template content:
{#
This template has been pulled from GitHub.
Uploaded to Cisco DNA Center by GitHub_Sync App
Author: gzapodea@cisco.com
Date: 2023-03-30T05:34:37Z
Commit message: updated logging and ntp servers
Commit URL: https://github.com/zapodeanu/dnacenter_github_templates/commit/04266ee7e1919d2ee0...
Commit Diff: @@ -1,7 +1,7 @@
 !
-logging buffered 4096
+logging buffered 81920
 logging host 10.93.141.37 transport udp port 8514
-logging source-interface Loopback1
+logging source-interface Loopback100
 no logging host 10.93.141.1 transport udp port 8514
 !
 service timestamps debug datetime localtime
#}
!
!
logging buffered 81920
logging host 10.93.141.37 transport udp port 8514
logging source-interface Loopback100
no logging host 10.93.141.1 transport udp port 8514
!
service timestamps debug datetime localtime
service timestamps log datetime localtime
!
INFO:root: New template "csr_logging" created
INFO:root: Task id: c1f0c20f-7765-4a81-adde-07870ff74ea0
INFO:root: Template "csr_logging" committed

INFO:root: Template name: snmp_ntp
INFO:root: Template content:
{#
This template has been pulled from GitHub.
Uploaded to Cisco DNA Center by GitHub_Sync App
Author: gzapodea@cisco.com
Date: 2023-03-30T05:36:35Z
Commit message: updated ntp server
Commit URL: https://github.com/zapodeanu/dnacenter_github_templates/commit/a21885aaa26fbf863...
Commit Diff: @@ -3,7 +3,7 @@ snmp-server host 10.93.135.30 version 2c RO
 snmp-server host 10.93.130.50 version 2c RW
 !
 ntp server 171.68.48.78
-ntp server 171.68.38.68
+ntp server 171.68.38.53
 no ntp server 171.68.48.80
 ntp source Loopback1
 !
\ No newline at end of file
#}
!
!
snmp-server host 10.93.135.30 version 2c RO
snmp-server host 10.93.130.50 version 2c RW
!
ntp server 171.68.48.78
ntp server 171.68.38.53
no ntp server 171.68.48.80
ntp source Loopback1
!
INFO:root: Template "snmp_ntp" has changed, different template on Cisco DNA Center
INFO:root: Updating existing template "snmp_ntp" id: 27c20fe5-b66b-4884-8d82-94c841805cff
INFO:root: Template "snmp_ntp" committed

INFO:root:
GitHub Sync Report:
Template "aaa_config" has not changed, identical template on Cisco DNA Center
New template "csr_logging" created and committed
Template "snmp_ntp" has changed, updated and committed on Cisco DNA Center

INFO:root: End of Application "dnacenter_github_sync.py" Run: 2023-04-03 19:33:09

```

Sample output **GitLab Sync**:


```shell
# Cisco DNA Center
DNAC_URL = 'https://dnacenter'
DNAC_USER = 'user'
DNAC_PASS = 'password'
DNAC_PROJECT = 'Cisco DNA Center Project'

# GitLab
GITLAB_TOKEN = 'token'   # GitLab access token
GITLAB_USERNAME = 'user'
GITLAB_REPO = 'repo'
DNAC_PROJECT = 'Cisco DNA Center Project'
```

Sample Output:

```shell
python dnacenter_gitlab_sync.py

INFO:root: App "dnacenter_gitlab_sync.py" Start, 2023-04-02 13:30:35
INFO:root: Repo "dnacenter_gitlab_templates" found!
INFO:root: Project id:  44770106
INFO:root: Repo "dnacenter_gitlab_templates" files:
INFO:root: File: aaa_config.txt
INFO:root: File: csr_logging.txt
INFO:root: File: snmp_ntp.txt
INFO:root: Project "GitLab_Project" id: 89f140f0-2776-...
INFO:root: Collected all commit comments for "dnacenter_gitlab_templates" repo, file: aaa_config.txt
INFO:root: Template name: aaa_config
INFO:root: Template content:
{#
This template has been pulled from GitLab.
Uploaded to Cisco DNA Center by GitLab_Sync App
Committer Name: gzapodea
Date: 2023-03-31T20:02:37.000-07:00
Commit message: change aaa-new-model - "no aaa new-model"
Commit URL: https://gitlab.com/zapodeanu/dnacenter_gitlab_templates/-/commit/9422f70c8b7...
Commit Diff: @@ -1,5 +1,6 @@
 !
-aaa new-model
+no aaa new-model
 aaa authentication login default local
 aaa authorization exec default local
+!
 !

#}
!
!
no aaa new-model
aaa authentication login default local
aaa authorization exec default local
!
!
INFO:root: New template "aaa_config" created
INFO:root: Task id: 5bfcc427-2edb-4563-9a9e-a29a8ec0e264
INFO:root: Template "aaa_config" committed

INFO:root: Collected all commit comments for "dnacenter_gitlab_templates" repo, file: csr_logging.txt
INFO:root: Template name: csr_logging
INFO:root: Template content:
{#
This template has been pulled from GitLab.
Uploaded to Cisco DNA Center by GitLab_Sync App
Committer Name: gzapodea
Date: 2023-04-01T18:05:26.000-07:00
Commit message: updated "logging buffered 40960"
updated "ntp server 171.68.38.63"
Commit URL: https://gitlab.com/zapodeanu/dnacenter_gitlab_templates/-/commit/065823320ff9c3...
Commit Diff: @@ -1,5 +1,5 @@
 !
-logging buffered 4096
+logging buffered 40960
 logging host 10.93.141.37 transport udp port 8514
 logging source-interface Loopback100
 no logging host 10.93.141.1 transport udp port 8514

#}
!
!
logging buffered 40960
logging host 10.93.141.37 transport udp port 8514
logging source-interface Loopback100
no logging host 10.93.141.1 transport udp port 8514
!
service timestamps debug datetime localtime
service timestamps log datetime localtime
!
INFO:root: Template "csr_logging" has not changed, identical template on Cisco DNA Center
INFO:root: Collected all commit comments for "dnacenter_gitlab_templates" repo, file: snmp_ntp.txt
INFO:root: Template name: snmp_ntp
INFO:root: Template content:
{#
This template has been pulled from GitLab.
Uploaded to Cisco DNA Center by GitLab_Sync App
Committer Name: gzapodea
Date: 2023-04-02T13:29:40.000-07:00
Commit message: changed snmp and ntp server info
Commit URL: https://gitlab.com/zapodeanu/dnacenter_gitlab_templates/-/commit/fa2175d296e3294d1...
Commit Diff: @@ -1,9 +1,9 @@
 !
 snmp-server host 10.93.135.30 version 2c RO
-snmp-server host 10.93.130.50 version 2c RW
+snmp-server host 10.93.130.30 version 2c RW
 !
 ntp server 171.68.48.78
-ntp server 171.68.38.63
+no ntp server 171.68.38.63
 no ntp server 171.68.48.80
 ntp source Loopback1
 !
\ No newline at end of file

#}
!
!
snmp-server host 10.93.135.30 version 2c RO
snmp-server host 10.93.130.30 version 2c RW
!
ntp server 171.68.48.78
no ntp server 171.68.38.63
no ntp server 171.68.48.80
ntp source Loopback1
!
INFO:root: Template "snmp_ntp" has changed, different template on Cisco DNA Center
INFO:root: Updating existing template "snmp_ntp" id: 8b4abd92-1ca7-4c1b-affb-c216a5b7c8f6
INFO:root: Template "snmp_ntp" committed

INFO:root:
GitLab Sync Report:
New template "aaa_config" created and committed
Template "csr_logging" has not changed, identical template on Cisco DNA Center
Template "snmp_ntp" has changed, updated and committed on Cisco DNA Center

INFO:root: End of Application "dnacenter_gitlab_sync.py" Run: 2023-04-02 13:31:04

```


**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).


