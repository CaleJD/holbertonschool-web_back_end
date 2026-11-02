#!/usr/bin/env python3
"""Generate multiple wait_randoms"""

import asyncio
import importlib
wait_random = importlib.import_module("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay: int = 10) -> list:
    """Spawns "n" amount of wait_random"""
    spawns = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(spawns)
