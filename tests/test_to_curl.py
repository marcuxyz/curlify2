import httpx
import requests
import responses
from curlify2 import to_curl

URL = "http://1.1.1.1"


@responses.activate
def test_returns_curl_string_using_requests_module():
    responses.add(responses.POST, URL)
    response = requests.post(URL)
    curl = to_curl(response.request)
    assert (
        curl
        == 'curl -X POST -H "User-Agent: python-requests/2.26.0" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Connection: keep-alive" -H "Content-Length: 0" -d \'None\' http://1.1.1.1/'
    )


def test_returns_curl_string_using_httpx_module(httpx_mock):
    httpx_mock.add_response()

    with httpx.Client() as client:
        response = client.get("http://test_url")
        curl = to_curl(response.request)
        assert (
            curl
            == 'curl -X GET -H "host: test_url" -H "accept: */*" -H "accept-encoding: gzip, deflate" -H "connection: keep-alive" -H "user-agent: python-httpx/0.16.1" -d '
            "'"
            "b"
            "'"
            ""
            "'"
            ""
            "'"
            " http://test_url"
        )
