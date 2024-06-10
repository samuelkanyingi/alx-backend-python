#!/usr/bin/env python3
''' Let's execute multiple coroutines at the same time with async '''
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' function for coroutinne '''
    tasks = list[wait_random(max_delay) for _ in range(n)]
    delays = list[]
    for task in asyncio.as_completed(tasks):
        delay: float = await task
        delays.append(delay)
    return delays
