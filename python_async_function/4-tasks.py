#!/usr/bin/env python3
"""Generate multiple task_wait_randoms"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns "n" amount of task_wait_random"""
    n_runs = []
    delays = []

    for i in range(n):
        n_runs.append(task_wait_random(max_delay))

    for run in asyncio.as_completed(n_runs):
        delay = await run
        delays.append(delay)

    return delays
