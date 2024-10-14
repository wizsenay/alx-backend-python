#!/usr/bin/env python3
"""
0-basic_async_syntax.py

 this modules is an asynchronous coroutine that takes in an integer argument
... and waits for a random delay between 0 and the given integer seconds and
... eventually returns it

Functions:
    wait_random = wate to a randem number and return it
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
        wait tile to 'delay' secound
    Arg:
       max_delay: the maximum time to stop the program from ranning
    Return:
       how many secound it stops
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
