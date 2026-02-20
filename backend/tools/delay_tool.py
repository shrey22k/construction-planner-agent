import random

def simulate_delay(task):
    """Simulate unexpected delay"""
    delayed = random.choice([True, False, False])
    if delayed:
        return f"Delay occurred in {task}"
    return None
