#!/usr/bin/env python3
"""Waits a random time and returns a task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns the task"""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
