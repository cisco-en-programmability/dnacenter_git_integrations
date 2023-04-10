#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Gabriel Zapodeanu TME, ENB"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import os
import time

import requests
from dotenv import load_dotenv

load_dotenv('environment.env')

GITLAB_USERNAME = os.getenv('GITLAB_USERNAME')
GITLAB_TOKEN = os.getenv('GITLAB_TOKEN')
GITLAB_REPO = os.getenv('GITLAB_REPO')

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

GITLAB_URL = 'https://gitlab.com/api/v4/'


def get_projects(gitlab_token):
    """
    This function will return all projects for authenticated user
    :param: gitlab_token: user personal token
    :return: projects_list
    """
    url = GITLAB_URL + '/projects?owned=true'
    header = {'Accept': 'application/json', 'PRIVATE-TOKEN': gitlab_token}
    response = requests.get(url, headers=header, verify=True)
    projects_list = response.json()
    return projects_list


def get_repository_tree(project_id, gitlab_token):
    """
    This function will get a list of repository files and directories in a project
    :param project_id: GitLab project id
    :param gitlab_token: user personal token
    :return: repo tree
    """
    url = GITLAB_URL + '/projects/' + str(project_id) + '/repository/tree'
    header = {'Accept': 'application/json', 'PRIVATE-TOKEN': gitlab_token}
    response = requests.get(url, headers=header, verify=True)
    tree_info = response.json()
    return tree_info


def get_repository_commits_for_file(project_id, filepath, gitlab_token):
    """
    The function will retrieve the commits' info for a file
    :param project_id: GitLab project id
    :param filepath: filepath
    :param gitlab_token: user personal token
    :return: repo commits
    """
    url = GITLAB_URL + '/projects/' + str(project_id) + '/repository/commits?path=' + filepath
    header = {'Accept': 'application/json', 'PRIVATE-TOKEN': gitlab_token}
    response = requests.get(url, headers=header, verify=True)
    commits_list = response.json()
    return commits_list


def get_file_from_repository(project_id, filepath, gitlab_token):
    """
    This function will retrieve the file info from repo - name, size, commit info
    :param project_id: GitLab project id
    :param filepath: filepath
    :param gitlab_token: user personal token
    :return: file info
    """
    url = GITLAB_URL + '/projects/' + str(project_id) + '/repository/files/' + filepath + '?ref=main'
    header = {'Accept': 'application/json', 'PRIVATE-TOKEN': gitlab_token}
    response = requests.get(url, headers=header, verify=True)
    file_info = response.json()
    return file_info


def get_file_raw_from_repository(project_id, filepath, gitlab_token):
    """
    This function will retrieve raw file from repo
    :param project_id: GitLab project id
    :param filepath: filepath
    :param gitlab_token: user personal token
    :return: raw file content
    """
    url = GITLAB_URL + '/projects/' + str(project_id) + '/repository/files/' + filepath + '/raw?ref=main'
    header = {'Accept': 'application/json', 'PRIVATE-TOKEN': gitlab_token}
    response = requests.get(url, headers=header, verify=True)
    raw_file_info = response.text
    return raw_file_info


def get_gitlab_commit_diff(project_id, commit_id, gitlab_token):
    """
    This function will return the diff for a commit in project
    :param project_id: GitLab project id
    :param commit_id: commit id
    :param gitlab_token: user personal token
    :return:
    """
    url = GITLAB_URL + '/projects/' + str(project_id) + '/repository/commits/' + commit_id + '/diff'
    header = {'Accept': 'application/json', 'PRIVATE-TOKEN': gitlab_token}
    response = requests.get(url, headers=header, verify=True)
    commit_diff = response.json()
    return commit_diff

