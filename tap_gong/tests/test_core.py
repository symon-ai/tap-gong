"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_gong.tap import TapGong

_ISO_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime(_ISO_FORMAT),
    "end_date": (
        datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)
    ).strftime(_ISO_FORMAT),
    "access_key": "foo",
    "access_key_secret": "bar"
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapGong,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()
