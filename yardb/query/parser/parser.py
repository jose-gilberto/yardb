from yardb.query.parser.ast.structures import TableStructure
from yardb.query.parser.ast.statements import SelectStatement
from yardb.query.parser.ast.operations import ProjectionOperation
from .lexer import Lexer, TokenKind


class Parser:

    lexer: Lexer

    def __init__(self, lexer: Lexer) -> None:
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self):
        raise Exception(f'ERR - Parser error : unknown token {self.current_token}.')
    
    def eat(self, token_kind: TokenKind):
        if self.current_token.kind == token_kind:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def statement(self):
        token = self.current_token
        if token.kind == TokenKind.SELECT:
            self.eat(TokenKind.SELECT)
            stmt = self.select_statement()
            self.eat(TokenKind.SEMICOLON)
            return stmt
    
    def select_statement(self):
        token = self.current_token
        
        self.eat(TokenKind.ASTERISK)
        self.eat(TokenKind.FROM)

        table_name = self.current_token.value
        self.eat(TokenKind.ID)

        return SelectStatement(
            ProjectionOperation(
                TableStructure(table_name)
            )
        )

    def parser(self):
        return self.statement()