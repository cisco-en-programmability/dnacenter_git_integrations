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

import base64
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv('environment.env')

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPO = os.getenv('GITHUB_REPO')

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

GITHUB_URL = 'https://api.github.com'


def get_repos(username):
    """
    This function will return all repos for user
    :param: username: user for which to return the repos
    :return: repos_list
    """
    url = GITHUB_URL + '/users/' + username + '/repos?per_page=100&sort=updated&direction=desc'
    header = {'Accept': 'application/vnd.github+json', 'Authorization': 'token ' + GITHUB_TOKEN}
    response = requests.get(url, headers=header, verify=True)
    response_json = response.json()
    repos_list = []
    for repo in response_json:
        repos_list.append(repo['name'])
    return repos_list


def get_repo_content(username, repo_name):
    """
    This function will return the contents of a repository
    :param: username: user for which to return the repos
    :param: repo_name: repository name
    :return: repos_list
    """
    url = GITHUB_URL + '/repos/' + username + '/' + repo_name + '/contents'
    header = {'Accept': 'application/vnd.github+json', 'Authorization': 'token ' + GITHUB_TOKEN}
    response = requests.get(url, headers=header, verify=True)
    response_json = response.json()
    files_list = []
    for file in response_json:
        files_list.append(file['name'])
    return files_list


def get_repo_file_content(username, repo_name, file_name):
    """
    This function will return the content of the file from the repo
    :param username: GitHub username
    :param repo_name: GitHub repo
    :param file_name: file name
    :return: return the file content
    """
    url = GITHUB_URL + '/repos/' + username + '/' + repo_name + '/contents/' + file_name
    header = {'Authorization': 'token ' + GITHUB_TOKEN}
    response = requests.get(url, headers=header)
    response_json = response.json()
    file_content = response_json['content']
    file_content_encoding = response_json.get('encoding')
    if file_content_encoding == 'base64':
        file_content = base64.b64decode(file_content).decode()
    return file_content


def get_repo_commits(username, repo_name):
    """
    This function will return all repo SHA for commits
    :param: username: user for which to return the repos
    :param: repo_name: repository name
    :return: SHA list
    """
    url = GITHUB_URL + '/repos/' + username + '/' + repo_name + '/commits'
    header = {'Accept': 'application/vnd.github+json', 'Authorization': 'token ' + GITHUB_TOKEN}
    response = requests.get(url, headers=header, verify=True)
    response_json = response.json()
    sha_list = []
    for commit in response_json:
        sha_list.append(commit['sha'])
    return sha_list


def get_repo_commit_sha(username, repo_name, sha):
    """
    This function will return commits details: author, message, date, file
    :param: username: user for which to return the repos
    :param: repo_name: repository name
    :param: sha: commit sha
    :return: commits details
    """
    url = GITHUB_URL + '/repos/' + username + '/' + repo_name + '/commits/' + sha
    header = {'Accept': 'application/vnd.github+json', 'Authorization': 'token ' + GITHUB_TOKEN}
    response = requests.get(url, headers=header, verify=True)
    response_json = response.json()
    commit_author = response_json['commit']['author']['email']
    commit_date = response_json['commit']['author']['date']
    commit_message = response_json['commit']['message']
    commit_file = response_json['files'][0]['filename']
    commit_url = response_json['html_url']
    commit_diff = response_json['files'][0]['patch']
    commit_info = {'filename': commit_file, 'date': commit_date, 'message': commit_message, 'url': commit_url, 'author': commit_author, 'diff': commit_diff}
    return commit_info
