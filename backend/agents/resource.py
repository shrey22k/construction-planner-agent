from tools.resource_tool import check_resources

class ResourceAgent:

    def validate(self, tasks):
        valid = []
        delayed = []

        for t in tasks:
            if check_resources(t["task"]):
                valid.append(t["task"])
            else:
                delayed.append(t["task"])

        return valid, delayed
