import httpx
import requests
import responses
from curlify2 import Curlify

URL = "http://127.0.0.1/json"


@responses.activate
def test_must_return_string_from_requests_via_get():
    responses.get(URL)
    response = requests.get(URL)
    curl_command = Curlify(response.request)

    assert (
        curl_command.to_curl()
        == 'curl -X GET -H "User-Agent: python-requests/2.31.0" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Connection: keep-alive" -d \'None\' http://127.0.0.1/json'
    )


@responses.activate
def test_must_return_string_from_requests_via_post():
    responses.post(URL)
    request = requests.post(URL)
    curl_command = Curlify(request.request)

    assert (
        curl_command.to_curl()
        == 'curl -X POST -H "User-Agent: python-requests/2.31.0" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Connection: keep-alive" -H "Content-Length: 0" -d \'None\' http://127.0.0.1/json'
    )


@responses.activate
def test_must_return_string_from_requests_via_put():
    responses.put(URL)
    request = requests.put(URL)
    curl_command = Curlify(request.request)

    assert (
        curl_command.to_curl()
        == 'curl -X PUT -H "User-Agent: python-requests/2.31.0" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Connection: keep-alive" -H "Content-Length: 0" -d \'None\' http://127.0.0.1/json'
    )


@responses.activate
def test_must_return_string_from_requests_via_delete():
    responses.delete(URL)
    request = requests.delete(URL, headers={"Content-Type": "application/json"})
    curl_command = Curlify(request.request)

    assert (
        curl_command.to_curl()
        == 'curl -X DELETE -H "User-Agent: python-requests/2.31.0" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Connection: keep-alive" -H "Content-Type: application/json" -H "Content-Length: 0" -d \'None\' http://127.0.0.1/json'
    )


def test_must_return_string_from_httpx_via_get(httpx_mock):
    httpx_mock.add_response()

    with httpx.Client() as client:
        response = client.get(URL)

        curl = Curlify(response.request).to_curl()
        breakpoint
        assert (
            curl
            == 'curl -X GET -H "host: 127.0.0.1" -H "accept: */*" -H "accept-encoding: gzip, deflate" -H "connection: keep-alive" -H "user-agent: python-httpx/0.24.1" -d '
            "'b''' "
            "http://127.0.0.1/json"
        )


def test_must_return_string_from_httpx_via_post(httpx_mock):
    httpx_mock.add_response()

    with httpx.Client() as client:
        response = client.post(URL, data={"name": "marcus"})

        curl = Curlify(response.request).to_curl()

        assert (
            curl
            == 'curl -X POST -H "host: 127.0.0.1" -H "accept: */*" -H "accept-encoding: gzip, deflate" -H "connection: keep-alive" -H "user-agent: python-httpx/0.24.1" -H "content-length: 11" -H "content-type: application/x-www-form-urlencoded" -d \'name=marcus\' http://127.0.0.1/json'
        )


def test_must_return_string_from_httpx_via_put(httpx_mock):
    httpx_mock.add_response()

    with httpx.Client() as client:
        response = client.put(URL, data={"id": 1, "name": "almeida"})

        curl_command = Curlify(response.request).to_curl()

        assert (
            curl_command
            == 'curl -X PUT -H "host: 127.0.0.1" -H "accept: */*" -H "accept-encoding: gzip, deflate" -H "connection: keep-alive" -H "user-agent: python-httpx/0.24.1" -H "content-length: 17" -H "content-type: application/x-www-form-urlencoded" -d \'id=1&name=almeida\' http://127.0.0.1/json'
        )


def test_must_return_string_from_httpx_via_delete(httpx_mock):
    httpx_mock.add_response()

    with httpx.Client() as client:
        response = client.delete(URL, params={"id": 1})

        curl_command = Curlify(response.request).to_curl()

        assert (
            curl_command
            == 'curl -X DELETE -H "host: 127.0.0.1" -H "accept: */*" -H "accept-encoding: gzip, deflate" -H "connection: keep-alive" -H "user-agent: python-httpx/0.24.1" -d \'b\'\'\' http://127.0.0.1/json?id=1'
        )
