import sys


def main():
    args = sys.argv[1:]

    if args[0] == 'cli':
        from .core.cli import CLI
        CLI.run()


if __name__ == '__main__':
    main()