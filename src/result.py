class Result:
    def __init__(self, path_to_goal, cost_of_path, nodes_expanded, search_depth, running_time):
        self.path_to_goal = path_to_goal
        self.cost_of_path = cost_of_path
        self.nodes_expanded = nodes_expanded
        self.search_depth = search_depth
        self.running_time = running_time
    