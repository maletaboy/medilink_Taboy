import os
import unittest
from unittest.mock import patch

from config import get_api_key, get_request_timeout


class ConfigurationTests(unittest.TestCase):
    def test_api_key_uses_local_fallback_when_unset(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(get_api_key(), "local-demo-key")

    def test_api_key_uses_environment_value(self) -> None:
        with patch.dict(os.environ, {"MEDILINK_API_KEY": "classroom-demo"}):
            self.assertEqual(get_api_key(), "classroom-demo")

    def test_timeout_defaults_to_five_seconds(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(get_request_timeout(), 5)

    def test_timeout_uses_environment_value(self) -> None:
        with patch.dict(os.environ, {"REQUEST_TIMEOUT": "12"}):
            self.assertEqual(get_request_timeout(), 12)

    def test_timeout_must_be_greater_than_zero(self) -> None:
        with patch.dict(os.environ, {"REQUEST_TIMEOUT": "0"}):
            with self.assertRaisesRegex(
                ValueError,
                "REQUEST_TIMEOUT must be greater than zero",
            ):
                get_request_timeout()

    def test_timeout_must_be_an_integer(self) -> None:
        with patch.dict(os.environ, {"REQUEST_TIMEOUT": "soon"}):
            with self.assertRaises(ValueError):
                get_request_timeout()


if __name__ == "__main__":
    unittest.main()
