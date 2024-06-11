#!/usr/bin/env python3
""" module to measure runtime of paallel comprehensions """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ measure runtime of an async comprehension"""
    start = time.perf_counter()
    task = asyncio.gather(async_comprehension(),async_comprehension(),
            async_comprehension(),async_comprehension())
    end = time.perf_counter()
    timeTaken = end - start
    return timeTaken
