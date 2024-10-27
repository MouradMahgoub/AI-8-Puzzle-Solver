import math


class EuclideanHeuristic:
    def calculate(self, state):
        state_str = str(state)
        if len(state_str) == 8:
            state_str = "0" + state_str

        goal_state = "012345678"
        h = 0

        for i in range(9):
            if state_str[i] != '0':
                goal_position = goal_state.index(state_str[i])
                vertical_difference = abs(i // 3 - goal_position // 3)
                horizontal_difference = abs(i % 3 - goal_position % 3)
                h += math.sqrt(vertical_difference ** 2 + horizontal_difference ** 2)

        return h
