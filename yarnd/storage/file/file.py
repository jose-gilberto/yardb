import os


def create_empty_file(path, nbytes):
    with open(path, 'wb') as file:
        file.seek(nbytes - 1)
        file.write(b'\0')
        file.close()
