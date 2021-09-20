from .overall_statements import TableListCommand, ExitCommand

overall_statements = {
    '.exit': ExitCommand().execute,
    '.tables': TableListCommand().execute
}


class CLI:

    @staticmethod
    def run():
        while True:
            input_buffer = input('yard > ')
            if input_buffer[0] == '.':
                if input_buffer not in overall_statements:
                    print(f'Unrecognized overall statement {input_buffer}.')
                else:
                    overall_statements[input_buffer]()
            else:
                print(f'Unrecognized statement {input_buffer}')