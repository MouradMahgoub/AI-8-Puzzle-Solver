from abc  import ABC, abstractmethod

class HeuristicStrategy(ABC):
    @abstractmethod
    def solve(self, puzzle):
        pass