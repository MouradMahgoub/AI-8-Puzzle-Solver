from strategies import SolverStrategy


class DFSSolver(SolverStrategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)

    def solve(self):
        depth_map = {self.puzzle.state: 0}
        self.start_timer()

        while self.frontier:
            current_state = self.frontier.pop()
            self.puzzle.state = current_state
            self.explored.add(current_state)

            if self.puzzle.is_goal():
                return self.get_result(current_state)

            neighbours = self.puzzle.get_neighbors()
            self.nodes_expanded += 1

            for neighbour in neighbours:
                if neighbour not in self.explored:
                    self.frontier.append(neighbour)
                    self.explored.add(current_state)
                    self.parent_map[neighbour] = current_state
                    depth_map[neighbour] = depth_map[current_state] + 1
                    self.max_depth = max(self.max_depth, depth_map[neighbour])

        return self.get_result(None)
