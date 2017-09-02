import logging; logging.basicConfig(level=logging.INFO)

import asyncio
from aiohttp import web


def index(request):
    return web.Response(body='<h1>Hello, young man</h1>', content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", index)
    srv = await loop.create_server(app.make_handler(), "127.0.0.1", 9000)
    logging.info("server stared at http://127.0.0.1:9000...")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()