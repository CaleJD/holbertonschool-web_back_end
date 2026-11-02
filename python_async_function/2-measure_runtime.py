#!/usr/bin/env python3
"""Measures runtime"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int = 10) -> float:
    """Calculates runtime"""
    start = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start
    end_time = (total_time / n)
    return end_time
