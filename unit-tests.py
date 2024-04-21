import unittest
from unittest.mock import patch
import json
from aws-json-verifier import verify_input

class TestVerifyInput(unittest.TestCase):

    def test_valid_json(self):
        json_data = {
            "PolicyName": "test",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": "arn:aws:iam::123456789012:user/*"
                    }
                ]
            }
        }
        with patch('builtins.open', side_effect=[json.dumps(json_data)]):
            self.assertTrue(verify_input("test.json"))

    def test_invalid_json(self):
        # Test with invalid JSON
        with patch('builtins.open', side_effect=[json.dumps({})]):
            self.assertFalse(verify_input("test.json"))

    def test_missing_resource_field(self):
        json_data = {
            "PolicyName": "test",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ]
                    }
                ]
            }
        }
        with patch('builtins.open', side_effect=[json.dumps(json_data)]):
            self.assertTrue(verify_input("test.json"))

    def test_resource_field_with_asterisk(self):
        json_data = {
            "PolicyName": "test",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": "*"
                    }
                ]
            }
        }
        with patch('builtins.open', side_effect=[json.dumps(json_data)]):
            self.assertFalse(verify_input("test.json"))

if __name__ == '__main__':
    unittest.main()
