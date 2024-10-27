import random
class Puzzle:
    goal_state = int("012345678")

    #directions = [-1, 1, -3, 3]

    # to do: precompute the neibours of each cell
    
    def __init__(self, state_str):
        self.state = self.state_to_int(state_str)
    
    def is_goal(self):
        # Implement goal check logic
        if self.state == self.goal_state:
            return True
        
        return False

    def swap_chars(self, s, i, j):
        s_list = list(s)         
        s_list[i], s_list[j] = s_list[j], s_list[i] 
        return ''.join(s_list) 
 

    """def valid_move(self, position, new_position):
        if new_position < 0 or new_position > 8:
            return False
        if abs(new_position - position) == 1 and int(position / 3) != int(new_position / 3):
            return False
        return True """

    def get_neighbors(self):
        # Implement logic to get neighboring states
        """current_state = self.state
        current_state = self.int_to_state(current_state)
        zero_position = current_state.index('0')
        child_states = []
        for direction in self.directions:
            new_position = zero_position + direction
            if self.valid_move(zero_position, new_position):
                child_states.append(self.state_to_int(self.swap_chars(current_state, zero_position, new_position))) 
        return child_states"""

        current_state = self.state
        current_state = self.int_to_state(current_state)
        zero_position = current_state.index('0')
        child_states = []
        #left position is valid if zero_position % 3 != 0 left position are: 0, 3, 6
        if zero_position % 3 != 0:
            child_states.append(self.state_to_int(self.swap_chars(current_state, zero_position, zero_position - 1)))
        #right position is valid if zero_position % 3 != 2 right position are: 2, 5, 8
        if zero_position % 3 != 2:
            child_states.append(self.state_to_int(self.swap_chars(current_state, zero_position, zero_position + 1)))
        #down position is valid if zero_position // 3 != 2 down position are not valid: 6, 7, 8
        if zero_position // 3 != 0:
            child_states.append(self.state_to_int(self.swap_chars(current_state, zero_position, zero_position - 3)))
        #up position is valid if zero_position // 3 != 0 up position are not valid: 0, 1, 2
        if zero_position // 3 != 2:
            child_states.append(self.state_to_int(self.swap_chars(current_state, zero_position, zero_position + 3)))
        return child_states

    def state_to_int(self, state_str):
        # Convert state to integer
        state_int = int(state_str)
        return state_int
    
    def int_to_state(self, state_int):
        # Convert integer to state
        state_str = str(state_int)
        if len(state_str) == 8: state_str = "0" + state_str
        return state_str

    
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