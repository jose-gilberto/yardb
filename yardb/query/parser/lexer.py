from enum import Enum


class TokenKind(Enum):
    EOF = -1
    ID = 1
    NUM = 2
    STR = 3

    SEMICOLON = 10
    ASTERISK = 15

    SELECT = 30
    FROM = 31


class Token:
    def __init__(self, kind: TokenKind, value) -> None:
        self.kind = kind
        self.value = value
    
    def __str__(self) -> str:
        return f'Token({self.kind}, {repr(self.value)})'

    def __repr__(self) -> str:
        return self.__str__()


class Lexer:

    current_char: str
    pos: int
    text: str

    def __init__(self, text) -> None:
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        
        self.reserved_keywords = {
            'SELECT': Token(TokenKind.SELECT, 'SELECT'),
            'FROM': Token(TokenKind.FROM, 'FROM')
        }

    def error(self):
        raise Exception(f'ERR - Lexical error: unknown char {self.current_char} at position {self.pos}.')
    
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def _id(self):
        lexem = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            lexem += self.current_char
            self.advance()
        
        token = self.reserved_keywords.get(lexem.upper(), Token(TokenKind.ID, lexem))
        return token

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return self._id()
            
            if self.current_char == '*':
                self.advance()
                return Token(TokenKind.ASTERISK, '*')
            
            if self.current_char == ';':
                self.advance()
                return Token(TokenKind.SEMICOLON, ';')
            
            self.error()
        
        return Token(TokenKind.EOF, '\0')
