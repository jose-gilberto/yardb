

def exit_command():
    exit(0)


def unrecognized_command(input_buffer):
    print(f'Unrecognized command \'{input_buffer}\'.')


READABLE_COMMANDS = {
    '.exit': exit_command
}


def execute_select():
    print('SELECT')


def execute_insert():
    print('INSERT')


READABLE_STATEMENTS = {
    'select': execute_select,
    'insert': execute_insert
}

class CommandReader:

    def __init__(self):
        pass

    def run(self):
        while True:
            input_buffer = input('yardb >> ')
            
            if input_buffer[0] == '.':
                if input_buffer not in READABLE_COMMANDS:
                    unrecognized_command(input_buffer)
                    continue
                READABLE_COMMANDS[input_buffer]()
                continue

            if input_buffer in READABLE_STATEMENTS:
                READABLE_STATEMENTS[input_buffer]()
                continue
            else:
                print(f'Unrecognized keyword at start of {input_buffer}.')
                continue


if __name__ == '__main__':
    CommandReader().run()
