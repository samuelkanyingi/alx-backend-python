#!/usr/bin/env python3
''' Measure the runtime '''
import time
import asyncio
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' measure runtime '''
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n
