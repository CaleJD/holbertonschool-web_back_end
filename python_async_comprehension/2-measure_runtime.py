#!/usr/bin/env python3
"""Measures the total runtime of 4 concurrent calls"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Runs 4 times in parallel and returns the total time"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
