"""Initial test file"""

from test_db import Test_db


def test_dummy():
    assert True


def test_connection():
    test_db_object = Test_db()

    assert test_db_object.test_connection() == "Connection successful"
