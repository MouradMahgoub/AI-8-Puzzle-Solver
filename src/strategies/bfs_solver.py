from collections import deque
from strategies import SolverStrategy
import time

class BFSSolver(SolverStrategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)

    def solve(self):
        self.frontier = deque(self.frontier)

        self.start_timer()
        while self.frontier:
            current_state =  self.frontier.popleft() 
            self.puzzle.state = current_state
            self.nodes_expanded += 1            
            if self.puzzle.is_goal():
                path = self.get_path(current_state)
                self.max_depth = len(path) - 1
                return self.get_result(current_state, path)

            # self.explored.add(current_state)  

            child_states = self.puzzle.get_neighbors()

            for child_state in child_states:
                if child_state not in self.parent_map:  # parent map -> explored U frontier
                    self.frontier.append(child_state)  
                    self.parent_map[child_state] = current_state
        return self.get_result(None)
