"""
JiraRequests.
"""


import requests


user = 'sokolok555@gmail.com'
apikey = 'PyWVaLgdloQm0MT1XrwW45CC'
server = 'https://jira-valeriy.atlassian.net'
data = '/rest/api/2/issue/'
auth = {
    "username": user,
    "password": apikey
}


def get_issue(key):
    json_data = requests.get(server + data + key, auth=(user, apikey)).json()
    stat = requests.get(server + data + key, auth=(user, apikey)).status_code
    issue = {
        "status_code": stat,
        "issue_summary": json_data["fields"]["summary"]
    }
    return issue
