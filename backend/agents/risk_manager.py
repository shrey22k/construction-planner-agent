class RiskManager:
    """
    Advanced Risk Analysis Engine
    """

    def recover(self, delayed_tasks):

        if not delayed_tasks:
            return (
                "✅ No major risks detected. "
                "All resources available and project is expected to proceed smoothly."
            )

        # Build professional risk message
        risk_msg = "⚠ Potential Project Risks Identified:\n\n"

        for task in delayed_tasks:
            risk_msg += f"• Delay risk in '{task}' due to resource constraints.\n"

        risk_msg += (
            "\nSuggested Mitigation:\n"
            "- Allocate backup resources\n"
            "- Adjust schedule buffer\n"
            "- Monitor critical path tasks\n"
        )

        return risk_msg
