"""
JiraRequests.
"""

import requests

user = 'mail@gmail.com'
api_key = 'key'
server = 'https://jira-valeriy.atlassian.net'
data = '/rest/api/2/issue'


def get_issue_by_id(key, fields='*all'):
    if fields != '*all':
        response = requests.get(server + data + '/' + key + '?fields=' + fields, auth=(user, api_key))
    else:
        response = requests.get(server + data + '/' + key, auth=(user, api_key))
    return response.status_code, response.json()


def create_issue(issue):
    response = requests.post(server + data, json=issue, auth=(user, api_key))
    return response.status_code, response.json()


def delete_issue(key):
    response = requests.delete(server + data + '/' + key, auth=(user, api_key))
    return response.status_code


def update_issue(key, issue):
    pass


def search_issue(criteria):
    pass
