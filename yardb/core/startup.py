import os
from abc import ABC, abstractmethod
from yardb import __version__


class Subsystem(ABC):
    """
    The subsystem can accept requests either from the facade or client directly.
    In any case, to the subsystem, the Facade is yet another client, and it's
    not a part of the Subsystem.
    """

    @abstractmethod
    def start(self):
        pass


# Facade pattern
class YardbFacade:
    """
    The Facade class provides a simple interface to the complex logic of
    the yardb subsystems. The Facade delegates the cliente requests to the 
    appropriate objects within the subsystem. The Facade is also responsible for
    managing their lifecycle. All of this shields the client for undesired 
    complexity of subsystems.
    
    - text by refactoring guru with some adaptations.

    """

    def __init__(self) -> None:
        self.subsystems = [ YardbFolderSystem() ]

    def start(self):
        for subsystem in self.subsystems:
            subsystem.start()


class YardbFolderSystem(Subsystem):

    ROOT_PATH = os.path.expanduser('~/.yardb/')
    CONF_PATH = os.path.expanduser('~/.yardb/yardb.conf')

    def create_folders(self) -> None:
        if os.path.isdir(YardbFolderSystem.ROOT_PATH):
            return
        
        os.makedirs(os.path.join(YardbFolderSystem.ROOT_PATH, 'base/public/tables'))
        os.makedirs(os.path.join(YardbFolderSystem.ROOT_PATH, 'base/public/views'))
        os.makedirs(os.path.join(YardbFolderSystem.ROOT_PATH, 'base/public/indexes'))

        os.makedirs(os.path.join(YardbFolderSystem.ROOT_PATH, 'base/template/tables'))
        os.makedirs(os.path.join(YardbFolderSystem.ROOT_PATH, 'base/template/views'))
        os.makedirs(os.path.join(YardbFolderSystem.ROOT_PATH, 'base/template/indexes'))

        with open(YardbFolderSystem.CONF_PATH, 'w') as conf_file:
            conf_file.write(f'VERSION:{__version__}\n')
            conf_file.write(f'CLUSTER:main')
            conf_file.close()
        
        return

    def start(self):
        self.create_folders()