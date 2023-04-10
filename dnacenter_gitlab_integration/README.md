# Cisco DNA Center GitLab Integration


This repo is for an application that will update and maintain in sync Cisco DNA Center Projects and CLI templates with a GitLab Repo hosting the templates files.
GitLab Repos will be used as a single source of truth for all desired settings, templates and profiles, providing consistent configurations across multiple Cisco DNA Center Clusters, lab and production.

**Cisco Products & Services:**

- Cisco DNA Center, devices managed by Cisco DNA Center
- Cisco DNA Center Python SDK

**Tools & Frameworks:**

- Python environment to run the application
- GitLab account, private token and repos
- Optional: CI/CD platform if desired to automate the process

**Usage**

This app will sync CLI templates from GitLab repos with Cisco DNA Center projects/templates:
 - identify if the specific project/repos exists in GitLab, pull or clone the repos.
 - will verify if the Cisco DNA Center template project exists and creates a new one
 - verify if Cisco DNA Center templates exist and are identical with the last version of the files from the GitLab repo
 - will create new templates or update existing ones with these details:
   - commit info: author, date, commit message and diff
   - CLI commands
 - it will commit the new or updated templates
 - no action will be taken if no templates changes
 - at the end of execution a report will be created
This app may be part of a CI/CD pipeline to run on-demand, scheduled or triggered by updates to the GitLab repo.

This app is using the Python SDK to make REST API calls to Cisco DNA Center.

Sample environment variables:

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


