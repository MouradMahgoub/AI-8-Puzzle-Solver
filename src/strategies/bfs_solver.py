from strategies import SolverStrategy
from puzzle import Puzzle

class BFSSolver(SolverStrategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)

    def solve(self):
        self.frontier = [self.puzzle.state]
        self.parent_map = {self.puzzle.state: None}  

        self.start_timer()

        while self.frontier:
            self.puzzle.state = self.frontier.pop(0)  
            self.nodes_expanded += 1            
            
            if self.puzzle.is_goal():
                path = self.get_path(self.puzzle.state)
                self.max_depth = len(path) - 1
                return self.get_result(self.puzzle.state, path)

            self.explored.add(self.puzzle.state)  

            child_states = self.puzzle.get_neighbors()

            for child_state in child_states:
                if child_state not in self.explored: 
                    self.frontier.append(child_state)  
                    self.parent_map[child_state] = self.puzzle.state

        return self.get_result(None)
