from strageties import SolverStrategy

class AStarSolver(SolverStrategy):
    def __init__(self, heuristic):
        self.heuristic = heuristic
    
    def solve(self, puzzle):
        # Implement A* algorithm here
        pass