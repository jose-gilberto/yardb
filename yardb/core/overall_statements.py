from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command/statement.
    """

    @abstractmethod
    def execute() -> None:
        pass


class ExitCommand(Command):
    """
    Command for exit the CLI Interface.
    """

    def __init__(self) -> None:
        super().__init__()
    
    def execute(self) -> None:
        print('Exiting the yardb cli interface...')
        exit(0)


class TableListCommand(Command):
    """
    Command to view the list of all tables in this database.
    """

    def __init__(self, database: str = 'public') -> None:
        super().__init__()
        self.database = database

    def execute(self) -> None:
        print(f'Listing all tables from {self.database}.')
