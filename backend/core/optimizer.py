class Optimizer:
    """
    Simple optimizer for ordering tasks based on estimated time.
    Can be extended for AI-based scheduling.
    """

    def optimize(self, schedule, estimates):
        return sorted(schedule, key=lambda t: estimates[t]["days"])
