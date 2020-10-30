def to_curl(request, compressed=False, verify=True) -> str:
    """to_curl function returns a string of curl to execute in shell.
    We accept 'requests' and 'httpx' module.
    """

    body = request.body if hasattr(request, "body") else request.read()
    headers = [f'"{k}: {v}"' for k, v in request.headers.items()]
    headers = " -H ".join(headers)

    if body and isinstance(body, bytes):
        body = body.decode()

    quote = f"curl -X {request.method} -H {headers} -d '{body}' {request.url}"

    if compressed:
        quote += " --compressed"
    if not verify:
        quote += " --insecure"

    return quote
