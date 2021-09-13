import sys


# size of a page in bytes
PAGE_SIZE = 8192


class HeapPage:

    # Loc pointer to the last line pointer
    pd_lower: int
    # Loc pointer to the last tuple
    pd_upper: int
    # line pointers
    line_pointers: list
    # tuples
    tuples: list

    def __init__(self):
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
    
    def write_page(self):
        self.pd_lower = 32 # doesnt have
        self.pd_upper = PAGE_SIZE - 1 - 255 - 16 # doesnt have

        bpd_lower = self.pd_lower.to_bytes(16, byteorder=sys.byteorder)
        bpd_upper = self.pd_upper.to_bytes(16, byteorder=sys.byteorder)

        with open('../../../.db/page.pg', 'wb') as file:
            file.seek(PAGE_SIZE - 1)
            file.write(b'\0')
            file.close()
        
        with open('../../../.db/page.pg', 'wb') as file:
            file.seek(0)
            file.write(bpd_lower)
            
            file.seek(16)
            file.write(bpd_upper)
            
            file.seek(32)
            file.write(int(PAGE_SIZE - 1).to_bytes(16, byteorder=sys.byteorder))

            file.seek(PAGE_SIZE - 1 - 255)
            file.write(b'table')

            file.seek(PAGE_SIZE - 1 - 255 - 16)
            file.write(int(1856523).to_bytes(16, byteorder=sys.byteorder))

            file.close()


    def read_page(self):
        with open('../../../.db/page.pg', 'rb') as file:
            file.seek(0)
            
            bpd_lower = file.read(16)
            self.pd_lower = int.from_bytes(bpd_lower, byteorder=sys.byteorder)
            print(self.pd_lower)
            
            file.seek(16)
            bpd_upper = file.read(16)
            self.pd_upper = int.from_bytes(bpd_upper, byteorder=sys.byteorder)
            print(self.pd_upper)

            file.seek(self.pd_lower)
            baddr_t1 = file.read(16)
            addr = int.from_bytes(baddr_t1, byteorder=sys.byteorder)
            print(addr)

            file.seek(addr - 255 - 16)
            b_oid = file.read(16)
            oid = int.from_bytes(b_oid, byteorder=sys.byteorder)
            print(oid)

            file.seek(addr - 255)
            b_tname = file.read(255)
            tname = b_tname.decode('utf-8')
            print(tname)



if __name__ == '__main__':
    HeapPage().read_page()
