from .ast import AST


class ProjectionOperation(AST):

    def __init__(self, operation) -> None:
        super().__init__()
        self.operation = operation

    def visit(self):
        pass

    def __repr__(self) -> str:
        return f'π( {str(self.operation)} )'

    def __str__(self) -> str:
        return self.__repr__()