from puzzle import Puzzle
from strategies import SolverStrategy


class DFSSolver(SolverStrategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)

    def solve(self):
        self.start_timer()
        depth_map = {self.puzzle.state: 0}

        while self.frontier:
            current_state = self.frontier.pop()
            self.puzzle.state = current_state
            current_depth = depth_map[current_state]
            self.explored.add(current_state)
            self.max_depth = max(self.max_depth, current_depth)

            if self.puzzle.is_goal():
                return self.get_result(current_state)

            neighbours = self.puzzle.get_neighbors()
            self.nodes_expanded += 1

            for neighbour in neighbours:
                if neighbour not in self.explored and neighbour not in self.frontier:
                    self.frontier.append(neighbour)
                    self.parent_map[neighbour] = current_state
                    depth_map[neighbour] = current_depth + 1

        return self.get_result(None)
