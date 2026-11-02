#!/usr/bin/env python3
"""A function to start a coroutine for a random time"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Generates a random number and waits"""
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
