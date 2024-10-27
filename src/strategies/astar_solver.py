from queue import PriorityQueue

from strategies import SolverStrategy

class AStarSolver(SolverStrategy):
    def __init__(self, puzzle, heuristic):
        super().__init__(puzzle, heuristic)

    def solve(self):
        self.start_timer()
        frontier = PriorityQueue()
        frontier.put((0, self.puzzle.state))
        depth_map = {self.puzzle.state: 0}

        while frontier:
            _, current_state = frontier.get()
            self.puzzle.state = current_state

            if self.puzzle.is_goal():
                return self.get_result(current_state)

            neighbours = self.puzzle.get_neighbors()
            self.nodes_expanded += 1

            for neighbour in neighbours:
                g = depth_map[current_state] + 1  # cost of path from start to current neighbour

                # we should update frontier only if: first appearance of neighbour or shorter path to neighbour
                if neighbour not in depth_map or g < depth_map[neighbour]:
                    h = self.heuristic.calculate(neighbour)  # heuristic value (cost to reach goal from curr neighbour)
                    frontier.put((h + g, neighbour))
                    self.parent_map[neighbour] = current_state
                    depth_map[neighbour] = g
                    self.max_depth = max(self.max_depth, depth_map[neighbour])

        return self.get_result(None)
