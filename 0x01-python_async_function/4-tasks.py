#!/usr/bin/env python3
""" wait task """
import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """co-routine for wait task"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
