import json
import pytest
from unittest.mock import patch
from src.lesson_12_1_11 import get_user_info, get_user_repos, get_github_users, get_currency_rate

"""Тесты 1 Задание"""


@patch("src.github.requests.get")
def test_get_user_info(mocked_get):
    mocked_get.return_value.status.code = 200
    mocked_get.return_value.json.return_value = {"login": "test_user", "public_repos": 10}
    result = get_user_info("test_user")
    assert result == (True, {"login": "test_user", "public_repos": 10})


@patch("src.github.requests.get")
def test_get_user_info_invalid(mocked_get):
    mocked_get.return_value.json.return_value = {"message": "Not Found"}
    result = get_user_info("non_existent_user")
    assert result == (False, {})


@patch("src.github.requests.get")
def test_get_user_repos(mocked_get):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
    result = get_user_repos("test_user")
    assert result == (True, ["repo1", "repo2"])


@patch("src.github.requests.get")
def test_get_user_repos_invalid(mocked_get):
    mocked_get.return_value.status_code = 404
    mocked_get.return_value.json.return_value = {"message": "Not Found"}
    result = get_user_repos("non_existent_user")
    assert result == (False, [])


@patch("src.github.git_user_info")
@patch("src.github.git_user_repos")
def test_get_github_users(mock_get_user_repos, mock_get_user_info):
    mock_get_user_info.return_value = (True, {"login": "user1", "public_repos": 2})
    mock_get_user_repos.return_value = (True, ["repo1", "repo2"])
    expected_result = [{"login": "user1", "public_repos": 2, "repositories": ["repo1", "repo2"]}]
    result = get_github_users(['user1'])
    assert result == json.dumps(expected_result)


@patch("src.github.git_user_info")
@patch("src.github.git_user_repos")
def test_get_github_users_negative(mock_get_user_repos, mock_get_user_info):
    mock_get_user_info.return_value = (False, {})
    mock_get_user_repos.return_value = (False, [])
    result = get_github_users(["non_existent_user"])
    assert result == "[]"


"""Тесты 2 Задание"""


def test_get_currency_rate(requests_mock):
    date = "2021-10-29"
    currency_code = "USD"

    requests_mock.get(
        f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js",
        json={
            "Value": {
                "USD": {"Value": 72.5},
                "EUR": {"Value": 84.8},
            },
        },
    )

    rate = get_currency_rate(date, currency_code)

    assert requests_mock.call_count == 1
    assert rate == {
        "date": date,
        "currency_code": currency_code,
        "rate": 72.5,
    }

    currency_code = "GBP"
    with pytest.raises(ValueError, match="No data for currency GBP"):
        rate = get_currency_rate(date, currency_code)

    requests_mock.get(
        f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js",
        status_code=404,
    )

    with pytest.raises(ValueError, match=f"Failed to get currency rate for date {date}"):
        rate = get_currency_rate(date, currency_code)
