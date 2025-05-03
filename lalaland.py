import asyncio

async def kids():
    print("We have kids")
    for i in range(0,6):
        await asyncio.sleep(1)
        print(f"We have kid {i}")

async def problems(delay):
    print("This is the start of problems")
    await asyncio.sleep(delay)
    print("We are done")

async def marriage():
    print("This is the start of the marriage")
    task = asyncio.create_task(problems(5))
    task1 = asyncio.create_task(kids())
    result,kiddies = await asyncio.gather(task,task1)
    print("Marriage is done")

asyncio.run(marriage())
#this is asynchronous programming the example above as well as the input below
#the best description of asynchronous programming
#when asyncio.run is executed it creates an event loop, functions with the async
#keyword creates a caroutine
#create_task add the caroutine to the event loop, whenever theres an await keyword
#the coroutine pauses, telling the manager(event loop), i need time to finish this task
#carry on with other things
#This is the start of the marriage
#This is the start of problems
#We have kids
#We have kid0
#We have kid1
#We have kid2
#We have kid3
#We are done
#We have kid4
#We have kid5
#Marriage is done
                              
