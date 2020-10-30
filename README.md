The library convert python 'requests' and 'httpx' object in curl command. Curlify2 is a enhancement of [curlify]('https://github.com/ofw/curlify').


## Installation

To install the library use pip or poetry command, see:

```bash
$ pip install curlify2
```

or poetry:

```bash
$ poetry add curlify2
```

## Usage

using **requests** module:

```python
import curlify2
import requests

URL = "https://run.mocky.io/v3/b0f4ffd8-6696-4f90-8bab-4a3bcad9ef3f"

request = requests.get(URL)
curl = curlify2.to_curl(request.request)

print(curl) # curl -X GET -H "User-Agent: python-requests/2.24.0" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Connection: keep-alive" -d 'None' https://run.mocky.io/v3/b0f4ffd8-6696-4f90-8bab-4a3bcad9ef3f

```

using **httpx** module:

```python
import curlify2
import httpx

URL = "https://run.mocky.io/v3/b0f4ffd8-6696-4f90-8bab-4a3bcad9ef3f"

request = httpx.get(URL)
curl = curlify2.to_curl(request.request)

print(curl) # curl -X GET -H "User-Agent: python-requests/2.24.0" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Connection: keep-alive" -d 'None' https://run.mocky.io/v3/b0f4ffd8-6696-4f90-8bab-4a3bcad9ef3f

```