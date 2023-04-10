# Cisco DNA Center GitHub Integration


This repo is for an application that will update and maintain in sync Cisco DNA Center Projects and CLI templates with a GitHub Repo hosting the templates files.
GitHub Repos will be used as a single source of truth for all desired settings, templates and profiles, providing consistent configurations across multiple Cisco DNA Center Clusters, lab and production.

**Cisco Products & Services:**

- Cisco DNA Center, devices managed by Cisco DNA Center
- Cisco DNA Center Python SDK

**Tools & Frameworks:**

- Python environment to run the application
- GitHub account, private token and repos
- Optional: CI/CD platform if desired to automate the process

**Usage**

This app will sync CLI templates from GitHub repos with Cisco DNA Center projects/templates:
 - identify if the specific repository exists in GitHub, pull or clone the repos.
 - will verify if the Cisco DNA Center template project exists and creates a new one
 - verify if Cisco DNA Center templates exist and are identical with the last version of the files from the GitHub repo
 - will create new templates or update existing ones with these details:
   - commit info: author, date, commit message and diff
   - CLI commands
 - it will commit the new or updated templates
 - no action will be taken if no templates changes
 - at the end of execution a report will be created
This app may be part of a CI/CD pipeline to run on-demand, scheduled or triggered by updates to the GitHub repo.

This app is using the Python SDK to make REST API calls to Cisco DNA Center.

Sample environment variables:

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

**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).


