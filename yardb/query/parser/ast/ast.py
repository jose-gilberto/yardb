from abc import ABC, abstractmethod


class AST(ABC):

    @abstractmethod
    def visit(self):
        pass
