#!/usr/bin/env python3
"""Waits a random time and returns a task"""

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Loops spawning tasks and returns the task"""
    loop = asyncio.get_event_loop()
    return loop.create_task(task_wait_random(max_delay))
