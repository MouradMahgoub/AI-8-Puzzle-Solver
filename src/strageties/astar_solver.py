from strageties import SolverStrategy

class AStarSolver(SolverStrategy):
    def __init__(self, puzzle, heuristic):
        super().__init__(puzzle)
        self.heuristic = heuristic
    
    def solve(self, puzzle):
        # Implement A* algorithm here
        pass