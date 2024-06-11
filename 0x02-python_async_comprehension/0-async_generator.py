#!/usr/bin/env python3
""" module for creating a Async Generator """

import asyncio
import random


async def async_generator():
    """  Async Generator """
    for i in range(10):
        random_num = random.random() * 10
        await asyncio.sleep(1)
        yield random_num
