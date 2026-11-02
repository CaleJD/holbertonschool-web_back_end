#!/usr/bin/env python3
"""Generate multiple wait_randoms"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawns "n" amount of wait_random"""
    n_runs = []
    delays = []

    for i in range(n):
        n_runs.append(wait_random(max_delay))

    for run in asyncio.as_completed(n_runs):
        delay = await run
        delays.append(delay)

    return delays
