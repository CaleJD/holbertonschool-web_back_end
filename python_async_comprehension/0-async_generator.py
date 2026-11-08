#!/usr/bin/env python3
"""Yields 10 values between 0-10"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times yielding a new number each time"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
