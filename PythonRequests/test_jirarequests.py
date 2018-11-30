"""
JiraRequests tests.
"""


import jirarequests


class TestJiraRequests:

    def test_login(self):
        assert 'OK' == jirarequests.login()
