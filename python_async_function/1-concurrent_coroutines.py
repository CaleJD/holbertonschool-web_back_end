#!/usr/bin/env python3
"""Generate multiple wait_randoms"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Spawns "n" amount of wait_random"""
    spawns = []
    for corout in asyncio.as_completed(
            [wait_random(max_delay) for i in range(n)]):
        spawns.append(await corout)
    return spawns
