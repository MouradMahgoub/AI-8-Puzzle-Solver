from abc  import ABC, abstractmethod
import time

from result import Result


class SolverStrategy(ABC):
    @abstractmethod
    def solve(self):
        pass 

    def __init__(self, puzzle, heuristic=None):
        self.puzzle = puzzle
        self.nodes_expanded = 0
        self.curr_depth = 0
        self.max_depth = 0
        self.frontier = [puzzle.state]
        # self.explored = set()
        self.parent_map = {puzzle.state: None}
        self.start_time = None
        self.heuristic = heuristic
        
    def start_timer(self):
        self.start_time = time.time()
    
    def stop_timer(self):
        return time.time() - self.start_time
    
    def get_path(self, goal_state):
        path = []
        state = goal_state
        while state is not None:
            path.append(self.puzzle.int_to_state(state))
            state = self.parent_map[state]
        path.reverse()
        return path
    
    def get_result(self, goal_state, path=None):
        running_time = self.stop_timer()
        
        if goal_state is None:
            return Result(None, 0, self.nodes_expanded, self.max_depth, running_time)

        if path is None:
            path = self.get_path(goal_state)

        return Result(path, len(path) - 1, self.nodes_expanded, self.max_depth, running_time)