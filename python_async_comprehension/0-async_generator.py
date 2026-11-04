#!/usr/bin/env python3
"""Yields 10 values between 0-10"""

import random
import asyncio

async def async_generator():
    """Loops 10 times yielding a new number each time"""
    for i in range(10):
        x = random.randint(0, 10)
        await asyncio.sleep(1)
        yield x
