import asyncio
from time import sleep, perf_counter

async def my_async_function():
    sleep(2)
    print(">>>>>>>>>>><<<<<<<<<<<")
    return True

# Use "to_thread" when you want the response of the async function in same manner as the code written
# async def async_function_call():
#     print(">>>>>>>>>>><<<<<<<<<<<0")
#     data = asyncio.to_thread(my_async_function)
#     await data
#     print(">>>>>>>>>>><<<<<<<<<<<1")


async def async_function_call():
    print(">>>>>>>>>>><<<<<<<<<<<0")
    asyncio.create_task(my_async_function())
    print(">>>>>>>>>>><<<<<<<<<<<1")
    
    
if __name__ == "__main__":
    time_before = perf_counter()
    asyncio.run(async_function_call())
    print("Time taken", perf_counter()-time_before)
