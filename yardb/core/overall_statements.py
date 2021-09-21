from abc import ABC, abstractmethod
from genericpath import isdir
from yardb import __version__
from .startup import YardbFolderSystem
import os

class Command(ABC):
    """
    The Command interface declares a method for executing a command/statement.
    """

    @abstractmethod
    def execute(self) -> None:
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


class VersionCommand(Command):
    """
    Command to view the actual version of the yardb dbms.
    """

    def __init__(self) -> None:
        super().__init__()

    def execute(self) -> None:
        print(f'Yardb version: {__version__}.')


class DatabaseListCommand(Command):
    """
    Command to list all the databases in this cluster.
    """

    def __init__(self) -> None:
        super().__init__()
    
    def execute(self) -> None:
        path = os.path.join(YardbFolderSystem.ROOT_PATH, 'base')
        databases_list = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
        print('Avaliable databases:')
        for db in databases_list:
            print(f'>>>\t{db}')
