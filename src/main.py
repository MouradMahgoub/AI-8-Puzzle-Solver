from strageties.bfs_solver import BFSSolver
from solver_factory import SolverFactory
from puzzle import Puzzle

def test_bfs_solver():
    puzzle = Puzzle("876543210")
    solver = SolverFactory.create_solver(puzzle, 'bfs')
    solver.start_timer()
    shortest_path = solver.solve()
    result = solver.path_results(shortest_path)
    print(f"Shortest Path:{result.path_to_goal}\nCost of the path:{result.cost_of_path}\nNodes Expanded:{result.nodes_expanded}\nSearch Depth:{result.search_depth}\nRunning time:{result.running_time}")

if __name__ == "__main__":
    test_bfs_solver()