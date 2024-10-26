from strageties import SolverStrategy
from puzzle import Puzzle

class BFSSolver(SolverStrategy):
    def __init__(self, puzzle):
        super().__init__(puzzle)

    def solve(self):
        frontier = [self.puzzle]  
        visited = set()
        parents = {self.puzzle.state: None}  

        while frontier:
            current_puzzle = frontier.pop(0)  
            self.nodes_expanded += 1            
            
            if current_puzzle.is_goal(): 
                return self.get_path(parents, current_puzzle.state)

            visited.add(current_puzzle.state)  

            child_states = current_puzzle.get_neighbors()

            for child_state in child_states:
                child_puzzle = Puzzle(current_puzzle.int_to_state(child_state))
                if child_puzzle.state not in visited:
                    frontier.append(child_puzzle)  
                    parents[child_puzzle.state] = current_puzzle.state
        return None
    
    def path_results(self, path):
        self.max_depth = len(path) - 1
        return self.get_result(path[-1])


    
        
