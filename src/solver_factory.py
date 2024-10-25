from strageties import SolverStrategy, BFSSolver, DFSSolver, AStarSolver
from heuristics import HeuristicStrategy, EuclideanHeuristic, ManhattanHeuristic

class SolverFactory:
    @staticmethod
    def create_solver(puzzle, solver_strategy, heuristic_strategy=None):
        if solver_strategy == 'bfs':
            return BFSSolver(puzzle)
        elif solver_strategy == 'dfs':
            return DFSSolver(puzzle)
        elif solver_strategy == 'astar':
            if heuristic_strategy == 'manhattan':
                return AStarSolver(puzzle, ManhattanHeuristic())
            elif heuristic_strategy == 'euclidean':
                return AStarSolver(puzzle, EuclideanHeuristic())
            else:
                raise ValueError('Invalid heuristic strategy')
        else:
            raise ValueError('Invalid solver strategy')