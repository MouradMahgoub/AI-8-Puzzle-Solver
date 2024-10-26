from abc  import ABC, abstractmethod
import time
from result import Result

class SolverStrategy(ABC):
    @abstractmethod
    def solve(self, puzzle):
        pass 

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.nodes_expanded = 0
        self.curr_depth = 0
        self.max_depth = 0
        self.frontier = []
        self.explored = set()
        self.parent_map = {}
        self.start_time = None
        self.path = []
        
    def start_timer(self):
        self.start_time = time.time()
    
    def stop_timer(self):
        return time.time() - self.start_time
    
    def get_path(self, parents, goal_state):
        # Get the path from the start state to the goal state
        path = []
        state = goal_state
        while state is not None:
            path.append(state)
            state = parents[state]
        path.reverse()  
        self.path = path
        return path
    
    def get_result(self, goal_state):
        if goal_state is None:
            return Result(None, 0, self.nodes_expanded, self.max_depth, self.stop_timer())
        
        return Result(self.path, len(self.path), self.nodes_expanded, self.max_depth, self.stop_timer())
        pass