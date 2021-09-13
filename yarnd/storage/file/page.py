

class Page:
    """ Standard interface for pages used in the management system.
    """

    def __init__(self):
        pass

    def write_page(self) -> bytes:
        pass

    def read_page(self, page_path):
        pass

    @staticmethod
    def create_page(self, tuples = None) -> Page:
        pass

    def close_page(self):
        pass
