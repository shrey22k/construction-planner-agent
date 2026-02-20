import random

def check_resources(task):
    """
    Simulate resource availability.
    Increase failure chance for demo visibility.
    """
    return random.choice([True, True, False])
