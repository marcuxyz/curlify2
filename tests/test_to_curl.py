import httpx
import requests
from curlify2 import Curlify

URL = "http://1.1.1.1"


def test_returns_curl_string_using_requests_module():
    response = requests.get(URL)

    curl = Curlify(response.request).to_curl()

    assert (
        curl
        == 'curl -X GET -H "User-Agent: python-requests/2.31.0" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Connection: keep-alive" -d \'None\' https://1.1.1.1/'
    )


def test_returns_curl_string_using_httpx_module(httpx_mock):
    httpx_mock.add_response()

    with httpx.Client() as client:
        response = client.get("http://test_url")

        curl = Curlify(response.request).to_curl()

        assert (
            curl
            == 'curl -X GET -H "host: test_url" -H "accept: */*" -H "accept-encoding: gzip, deflate" -H "connection: keep-alive" -H "user-agent: python-httpx/0.24.1" -d '
            "'"
            "b"
            "'"
            ""
            "'"
            ""
            "'"
            " http://test_url"
        )
