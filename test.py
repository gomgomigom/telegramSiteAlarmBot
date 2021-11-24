from time import sleep
import asyncio


async def coroutine():
    print("coroutine")
    sleep(1)


async def coroutine2():
    print("coroutine2")
    sleep(1)


coroutine()


loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine2())
loop.close()
