import pytest


def get_data():
    return [

        ("trainer@way2automation.com", "kjsdfbksdf"),
        ("java@way2automation.com", "sdf"),
        ("info@way2automation.com", "sdfsdf")

    ]


@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    print(username, "---", password)
