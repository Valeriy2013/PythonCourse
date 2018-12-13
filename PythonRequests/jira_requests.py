"""
JiraRequests.
"""

import requests


def get_issue_by_id(key, fields='*all'):
    if fields != '*all':
        response = requests.get(credentials.server + endpoints.issue_endpoint + '/' + key + '?fields=' + fields, auth=(credentials.user, credentials.api_key))
    else:
        response = requests.get(credentials.server + endpoints.issue_endpoint + '/' + key, auth=(credentials.user, credentials.api_key))
    return response.status_code, response.json()


def create_issue(issue):
    response = requests.post(credentials.server + endpoints.issue_endpoint, json=issue, auth=(credentials.user, credentials.api_key))
    return response.status_code, response.json()


def create_issue_bulk(issue):
    response = requests.post(credentials.server + endpoints.issue_endpoint + '/bulk', json=issue, auth=(credentials.user, credentials.api_key))
    return response.status_code, response.json()


def delete_issue(key):
    response = requests.delete(credentials.server + endpoints.issue_endpoint + '/' + key, auth=(credentials.user, credentials.api_key))
    return response.status_code


def update_issue(key, issue):
    response = requests.put(credentials.server + endpoints.issue_endpoint + '/' + key, json=issue, auth=(credentials.user, credentials.api_key))
    return response.status_code


def search_issue(criteria):
    response = requests.post(credentials.server + endpoints.search_endpoint, json=criteria, auth=(credentials.user, credentials.api_key))
    return response.status_code, response.json()
