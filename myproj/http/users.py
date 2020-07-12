from aiohttp import web
from asyncworker import RouteTypes

from myproj.app import app


@app.route(["/users"], type=RouteTypes.HTTP, methods=["GET"])
async def get_users():
    return web.json_response({})
