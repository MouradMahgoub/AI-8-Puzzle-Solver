from abc  import ABC, abstractmethod

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
        
    def start_timer(self):
        self.start_time = time.time()
    
    def stop_timer(self):
        return time.time() - self.start_time
    
    def get_path(self, goal_state):
        # Get the path from the goal state to the start state
        pass
    
    def get_result(self, goal_state):
        # Construct the result object
        pass