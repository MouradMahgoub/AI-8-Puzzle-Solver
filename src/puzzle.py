import random
class Puzzle:
    # to do: precompute the neibours of each cell
    
    def __init__(self, state_str):
        self.state = self.state_to_int(state_str)
    
    def is_goal(self):
        # Implement goal check logic
        pass

    def get_neighbors(self):
        # Implement logic to get neighboring states
        pass
    
    def state_to_int(self, state_str):
        # Convert state to integer
        pass
    
    def int_to_state(self, state_int):
        # Convert integer to state
        pass
    
    @staticmethod
    def generate_solvable_state():
        state = list("123456780")
        while True:
            random.shuffle(state)
            if Puzzle.is_solvable(state):
                return "".join(state)
    
    @staticmethod
    def is_solvable(state):
        # Implement logic to check if the state is solvable
        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] != '0' and state[j] != '0' and state[i] > state[j]:
                    inversions += 1
        return inversions % 2 == 0