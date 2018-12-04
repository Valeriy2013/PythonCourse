"""
JiraRequests.
"""

import requests
import os

user = os.env("mail")
api_key = os.env("api_key")
server = 'https://jira-valeriy.atlassian.net'
issue_endpoint = '/rest/api/2/issue'
search_endpoint = '/rest/api/2/search'


def get_issue_by_id(key, fields='*all'):
    if fields != '*all':
        response = requests.get(server + issue_endpoint + '/' + key + '?fields=' + fields, auth=(user, api_key))
    else:
        response = requests.get(server + issue_endpoint + '/' + key, auth=(user, api_key))
    return response.status_code, response.json()


def create_issue(issue):
    response = requests.post(server + issue_endpoint, json=issue, auth=(user, api_key))
    return response.status_code, response.json()


def create_issue_bulk(issue):
    response = requests.post(server + issue_endpoint + '/bulk', json=issue, auth=(user, api_key))
    return response.status_code, response.json()


def delete_issue(key):
    response = requests.delete(server + issue_endpoint + '/' + key, auth=(user, api_key))
    return response.status_code


def update_issue(key, issue):
    response = requests.put(server + issue_endpoint + '/' + key, json=issue, auth=(user, api_key))
    return response.status_code


def search_issue(criteria):
    response = requests.post(server + search_endpoint, json=criteria, auth=(user, api_key))
    return response.status_code, response.json()
