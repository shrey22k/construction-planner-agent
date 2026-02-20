import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class LLMPlanner:
    """
    Groq-based AI Planner (FREE)
    """

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_tasks(self, goal):

        prompt = f"""
        You are a Construction Planning AI.
        Break the goal into ordered construction tasks with dependencies.

        Goal: {goal}

        Output STRICT JSON ONLY:
        [
          {{ "task": "", "depends_on": [] }}
        ]
        """

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )

            text = response.choices[0].message.content.strip()

            # Ensure JSON parsed safely
            if text.startswith("```"):
                text = text.split("```")[1]

            return json.loads(text)

        except Exception as e:
            print("⚠ Groq failed, using fallback planner:", e)

            # Fallback offline
            return [
                {"task": "Site Preparation", "depends_on": []},
                {"task": "Foundation", "depends_on": ["Site Preparation"]},
                {"task": "Structure Construction", "depends_on": ["Foundation"]},
                {"task": "Electrical Work", "depends_on": ["Structure Construction"]},
                {"task": "Plumbing", "depends_on": ["Structure Construction"]},
                {"task": "Finishing", "depends_on": ["Electrical Work", "Plumbing"]},
            ]
