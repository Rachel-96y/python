import time
import asyncio
async def func_1():
    await asyncio.sleep(7)
    print("123")
async def func_2():
    await asyncio.sleep(5)
    print("456")
async def func_3():
    await asyncio.sleep(6)
    print("789")

async def main():
    tasks = [asyncio.create_task(func_1()),
             asyncio.create_task(func_2()),
             asyncio.create_task(func_3())]
    await asyncio.wait(tasks)
    
if __name__ == "__main__":
    time_old = time.time()
    asyncio.run(main())
    time_new = time.time()
    time_all = time_new - time_old
    print(time_all)
