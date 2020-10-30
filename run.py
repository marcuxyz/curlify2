from curlify2.curlify import to_curl
import requests
import httpx

URL = "https://run.mocky.io/v3/b0f4ffd8-6696-4f90-8bab-4a3bcad9ef3f"

request = requests.get(URL)
request2 = httpx.get(URL)

print(to_curl(request.request))
# print(response2.read().decode())
print(to_curl(request2.request, True))
