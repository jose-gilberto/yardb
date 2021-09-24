from .ast import AST


class TableStructure(AST):

    def __init__(self, table_name: str) -> None:
        self.table_name = table_name

    def visit(self):
        pass

    def __repr__(self) -> str:
        return f'{self.table_name}'
    
    def __str__(self) -> str:
        return self.__repr__()
