from tools.cost_tool import estimate_cost_time

class CostEstimator:

    def estimate(self, tasks):
        result = {}

        for t in tasks:
            result[t] = estimate_cost_time(t)

        return result
