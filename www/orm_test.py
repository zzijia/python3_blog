import asyncio

from python3_blog.www import orm
from python3_blog.www.models import User


async def test(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User(name='first', email='first@qq.com', passwd='1223', image='123')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
__pool = orm.__pool
__pool.close()  # 需要先关闭连接池
loop.run_until_complete(__pool.wait_closed())
loop.close()