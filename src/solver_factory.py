from heuristics import EuclideanHeuristic, ManhattanHeuristic
from strategies import BFSSolver, DFSSolver, AStarSolver, IDSSolver


class SolverFactory:
    @staticmethod
    def create_solver(puzzle, solver_strategy):
        if solver_strategy == 'BFS':
            return BFSSolver(puzzle)
        elif solver_strategy == 'DFS':
            return DFSSolver(puzzle)
        elif solver_strategy == 'IDS':
            return IDSSolver(puzzle)
        elif solver_strategy == 'A*_Manhattan':
            return AStarSolver(puzzle, ManhattanHeuristic())
        elif solver_strategy == 'A*_Euclidean':
            return AStarSolver(puzzle, EuclideanHeuristic())
        else:
            return DFSSolver(puzzle)