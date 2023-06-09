class Curlify:
    def __init__(self, request, compressed=False, verify=True):
        self.req = request
        self.compressed = compressed
        self.verify = verify

    def to_curl(self) -> str:
        """to_curl function returns a string of curl to execute in shell.
        We accept 'requests' and 'httpx' module.
        """
        return self.quote()

    def headers(self) -> str:
        """organize headers

        Returns:
            str: return string of set headers
        """
        headers = [f'"{k}: {v}"' for k, v in self.req.headers.items()]

        return " -H ".join(headers)

    def body(self):
        if hasattr(self.req, "body"):
            return self.req.body

        return self.req.read()

    def body_decode(self):
        body = self.body()

        if body and isinstance(body, bytes):
            return body.decode()

        return body

    def quote(self) -> str:
        """build curl command

        Returns:
            str: string represents curl command
        """
        quote = f"curl -X {self.req.method} -H {self.headers()} -d '{self.body_decode()}' {self.req.url}"

        if self.compressed:
            quote += " --compressed"
        if not self.verify:
            quote += " --insecure"

        return quote
