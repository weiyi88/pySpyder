import time

#同步
# def hello():
#     time.sleep(1)
#
# def run():
#     for i in range(5):
#         hello()
#         print("hello world:%s"% time.time())
#
# if __name__ == '__main__':
#     print(__name__)
#     run()


import asyncio

async def func1():
    print(1)
    await asyncio.sleep(2)  # 耗时操作
    print(2)

async def func2():
    print(3)
    await asyncio.sleep(2)   # 耗时操作
    print(4)

tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
