from core.llm_planner import LLMPlanner

class PlannerAgent:
    def __init__(self):
        self.llm = LLMPlanner()

    def run(self, goal):
        return self.llm.generate_tasks(goal)
