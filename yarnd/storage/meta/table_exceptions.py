
class TableNotFoundException(Exception):

    def __init__(self, message = 'Table not found!'):
        super().__init__(message)
