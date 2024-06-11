#!/usr/bin/env python3
""" async comprehension """
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ async comprehension for random number """
    rand = [x  async for x in async_generator()]
    yield rand
