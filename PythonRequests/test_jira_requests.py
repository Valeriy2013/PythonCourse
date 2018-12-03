"""
JiraRequests tests.
"""
from PythonRequests import json_fixtures, jira_requests


class TestJiraRequests:

    def test_get_issue_by_id(self):
        status_code, response = jira_requests.get_issue_by_id('TES-1', 'summary,description')
        assert status_code == 200
        assert response['fields']['summary'] == 'test bug 1 summary'
        assert response['fields']['description'] == 'test bug 1 description'

    def test_create_issue(self):
        # create an issue
        path = "D:\\_Projects\\PythonCourse\\PythonRequests\\jsons\\issue_to_create.json"
        issue_to_create = json_fixtures.get_json_data(path)
        status_code, response = jira_requests.create_issue(issue_to_create)
        assert status_code == 201

        # get created issue and check fields
        new_key = response['key']
        get_status_code, get_response = jira_requests.get_issue_by_id(new_key, 'summary,description')
        assert get_status_code == 200
        assert get_response['fields']['summary'] == "Created via REST"
        assert get_response['fields']['description'] == "Creating of an issue using project keys and issue type names using the REST API"

        # delete created issue
        jira_requests.delete_issue(new_key)

    def test_delete_issue(self):
        # crate issue for deletion
        path = "D:\\_Projects\\PythonCourse\\PythonRequests\\jsons\\issue_to_create.json"
        issue_to_create = json_fixtures.get_json_data(path)
        status_code, response = jira_requests.create_issue(issue_to_create)

        # delete issue
        new_key = response['key']
        del_code = jira_requests.delete_issue(new_key)
        assert del_code == 204

        # check issue not exist after deletion
        get_status_code, get_response = jira_requests.get_issue_by_id(new_key, 'summary,description')
        assert get_status_code == 404

    def test_update_issue(self):
        pass

    def test_search_issue(self):
        pass
