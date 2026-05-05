import httpx


class ApiKeyAuth(httpx.Auth):
    def __init__(self, key: str):
        self.key = key


    def auth_flow(self, request: httpx.Request):
        request.headers['X-API-KEY'] = self.key
        yield request
