import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def generate_gantt(schedule, estimates):
    if not schedule:
        return

    tasks = list(schedule)
    days = [estimates[t]["days"] for t in tasks]

    plt.figure(figsize=(10, 5))
    plt.barh(tasks, days)
    plt.xlabel("Days")
    plt.title("Construction Schedule Gantt Chart")

    plt.tight_layout()
    plt.savefig("gantt.png")
    plt.close()
