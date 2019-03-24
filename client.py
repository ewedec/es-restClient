import requests


class Client(object):

    def __init__(self):
        pass

    def __getattr__(self, attr_name):
        if attr_name == 'cookies':
            cookies = cache.get(settings.SSO_SESSION_COOKIES)
            if not cookies:
                request_session = requests.session()
                request_session.post(settings.SSO_LOGIN_URL, json={
                    "username": settings.SSO_USERNAME,
                    "password": settings.SSO_PASSWORD
                })
                cookies = dict(request_session.cookies.items())
                cache.set(settings.SSO_SESSION_COOKIES, cookies, timeout=settings.SSO_TIME_OUT)
            return cookies
        return None

    def get(self, *args, **kwargs):
        return requests.get(cookies=self.cookies, *args, **kwargs)

    def post(self, *args, **kwargs):
        return requests.get(cookies=self.cookies, *args, **kwargs)

    def patch(self, *args, **kwargs):
        return requests.patch(cookies=self.cookies, *args, **kwargs)

    def put(self, *args, **kwargs):
        return requests.put(cookies=self.cookies, *args, **kwargs)

    def delete(self, *args, **kwargs):
        return requests.delete(cookies=self.cookies, *args, **kwargs)
