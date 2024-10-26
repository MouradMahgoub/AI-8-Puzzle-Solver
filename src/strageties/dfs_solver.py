from src.puzzle import Puzzle
from src.strageties import SolverStrategy


class DFSSolver(SolverStrategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)

    def solve(self):
        self.start_timer()

        while self.frontier:
            current_state = self.frontier.pop()
            self.explored.add(current_state)
            puzzle = Puzzle(current_state)

            if puzzle.is_goal():
                return self.get_result(current_state)

            neighbours = puzzle.get_neighbors()

            for neighbour in neighbours:
                if neighbour not in self.explored and neighbour not in self.frontier:
                    self.frontier.append(neighbour)

        return self.get_result(None)
