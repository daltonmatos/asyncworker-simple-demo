from http import HTTPStatus

from asynctest import TestCase
from asyncworker.testing import HttpClientContext

from myproj.app import app
from myproj.http import users


class UsersEndpointTest(TestCase):
    async def test_get_users(self):
        async with HttpClientContext(app) as client:
            resp = await client.get("/users")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual({}, data)
