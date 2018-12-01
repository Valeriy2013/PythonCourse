"""
JiraRequests tests.
"""


import jirarequests


class TestJiraRequests:

    def test_get_issue(self):
        expected = {
            "status_code": 200,
            "issue_summary": "test bug 1"
        }
        assert str(expected) == str(jirarequests.get_issue('TES-1'))
