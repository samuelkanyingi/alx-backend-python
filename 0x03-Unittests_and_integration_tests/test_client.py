#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
from fixtures import TEST_PAYLOAD


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
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

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
        self.assertEqual(client._public_repos_url,
                         test_org_payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the correct list
        of repositories based on the mocked get_json method.
        """
        # Define the test payload and the expected URL
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        test_url = 'https://api.github.com/orgs/test-org/repos'

        # Mock the get_json method to return the test payload
        mock_get_json.return_value = test_payload

        # Patch the _public_repos_url property to return the test URL
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_url

            # Create an instance of GithubOrgClient
            client = GithubOrgClient('test-org')

            # Get the list of public repos
            repos = client.public_repos()

            # Verify that the public_repos method returns the expected payload
            self.assertEqual(repos, [repo['name'] for repo in test_payload])

            # Check that the _public_repos_url and get_json were called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license correctly identifies if a license
        key is present in the repo's license data.
        """
        # Check if the repo has the specified license key
        has_license = GithubOrgClient.has_license(repo, license_key)

        # Assert that has_license returns the expected result
        self.assertEqual(has_license, expected)


@parameterized_class((
        'org_payload',
        'repos_payload',
        'expected_repos',
        'apache2_repos'), TEST_PAYLOAD)
class MockResponse:
    """
    Mock the Response object returned by requests.get.
    """
    def __init__(self, json_data):
        """ initialize """
        self.json_data = json_data

    def json(self):
        """ json """
        return self.json_data


class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment by patching requests.get.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side effects for different URLs
        cls.mock_get.side_effect = lambda url: cls._get_payload_for_url(url)

    def test_public_repos(self):
        """
        Test that GithubOrgClient.public_repos returns the correct list
        of repositories based on the mocked get_json method.
        """
        client = GithubOrgClient('test-org')
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    @classmethod
    def _get_payload_for_url(cls, url):
        """
        Return the appropriate payload based on the URL.
        """
        if url == 'https://api.github.com/orgs/test-org':
            return MockResponse(cls.org_payload)
        elif url == 'https://api.github.com/orgs/test-org/repos':
            return MockResponse(cls.repos_payload)
        elif url == 'https://api.github.com/orgs/apache2/repos':
            return MockResponse(cls.apache2_repos)
        return MockResponse({})

    def test_public_repos(self):
        """
        Test that GithubOrgClient.public_repos returns the correct list
        of repositories based on the mocked get_json method.
        """
        client = GithubOrgClient('test-org')
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test that GithubOrgClient.public_repos returns the correct list
        of repositories filtered by license.
        """
        client = GithubOrgClient('test-org')
        # Assuming that `public_repos` accepts a license parameter
        repos = client.public_repos(license='apache-2.0')
        self.assertEqual(repos, [repo['name'] for repo in self.apache2_repos])

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test environment by stopping the patcher.
        """
        cls.get_patcher.stop()


class MockResponse:
    """
    Mock the Response object returned by requests.get.
    """
    def __init__(self, json_data):
        """ initialize """
        self.json_data = json_data

    def json(self):
        """ json """
        return self.json_data


if __name__ == '__main__':
    unittest.main()
