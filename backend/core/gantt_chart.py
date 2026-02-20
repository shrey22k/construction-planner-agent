import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def generate_gantt(schedule, estimates, path="gantt.png"):
    """Create a gantt chart image at the given path.

    Defaults to "gantt.png" but callers can supply any location (e.g. a
    temporary directory) so that the workspace itself is not modified. The
    return value is the same path for convenience.
    """

    if not schedule:
        return path

    tasks = list(schedule)
    days = [estimates[t]["days"] for t in tasks]

    plt.figure(figsize=(10, 5))
    plt.barh(tasks, days)
    plt.xlabel("Days")
    plt.title("Construction Schedule Gantt Chart")

    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path
