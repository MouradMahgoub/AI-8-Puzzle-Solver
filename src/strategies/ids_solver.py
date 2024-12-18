from strategies import SolverStrategy
from collections import deque

class IDSSolver(SolverStrategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)

    def solve(self):
        self.start_timer()
        initial_state = self.puzzle.state
        depth = 0
        while True:
            result = self.dls(depth, initial_state)
            if result is not None:
                return result
            depth += 1

    def dls(self, depth, initial_state):
        self.frontier = deque([initial_state])
        # self.explored = set()
        self.parent_map = {initial_state: None}
        depth_map = {initial_state: 0}

        while self.frontier:
            current_state = self.frontier.pop()
            current_depth = depth_map[current_state]
            self.puzzle.state = current_state
            self.max_depth = max(self.max_depth, depth)

            if self.puzzle.is_goal():
                return self.get_result(current_state)

            if current_depth < depth:
                # self.explored.add(current_state)
                neighbours = self.puzzle.get_neighbors()
                self.nodes_expanded += 1

                for neighbour in neighbours:
                    visited_but_in_higher_depth = neighbour in depth_map and depth_map[neighbour] > current_depth + 1

                    if neighbour not in depth_map or visited_but_in_higher_depth: # depth map -> explored U frontier
                        self.frontier.append(neighbour)
                        self.parent_map[neighbour] = current_state
                        depth_map[neighbour] = current_depth + 1
        return None
