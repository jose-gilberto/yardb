
class CommandReader:

    def __init__(self):
        pass

    def run(self):
        while True:
            input_buffer = input('yardb>> ')
            if input_buffer == '.exit':
                exit(0)
            else:
                print(f'Unrecognized command \'{input_buffer}\'.')
