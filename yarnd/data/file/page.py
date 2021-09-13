
# size of a page in bytes
PAGE_SIZE = 8192


class Page:

    # Loc pointer to the last line
    pd_lower: int
    # Loc pointer to the last tuple
    pd_upper: int

    def __init__(self) -> None:
        pass

    def mount_page():
        """
        #####################################
        #           PAGE STRUCTURE          #
        #####################################

        # [16 bits]
        # pd_lower [8 bits]
        # pd_upper [8 bits]

        # [size - 16 bits]
        
        E.g.: Insert one tuple
        #####################################
        # [32] [-1] | [-1]                  #
        #                                   #
        #                              [t1] #
        #####################################

        """
        ...