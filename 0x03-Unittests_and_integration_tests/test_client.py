#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit test class for GithubOrgClient.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        test_payload = {'login': org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url returns the correct URL
        based on the mocked org property.
        """
        test_org_payload = {
            'repos_url': 'https://api.github.com/orgs/test-org/repos'
        }
        mock_org.return_value = test_org_payload

        client = GithubOrgClient('test-org')
        self.assertEqual(client._public_repos_url, test_org_payload['repos_url'])


if __name__ == '__main__':
    unittest.main()
