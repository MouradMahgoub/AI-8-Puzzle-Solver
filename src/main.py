from strageties.bfs_solver import BFSSolver
from solver_factory import SolverFactory
from puzzle import Puzzle

def test_bfs_solver():
    puzzle = Puzzle("312045678")
    solver = SolverFactory.create_solver(puzzle, 'bfs')
    result = solver.solve()
    print("True" if result else "False")


if __name__ == "__main__":
    test_bfs_solver()
