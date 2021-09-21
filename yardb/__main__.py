import sys


def main():
    args = sys.argv[1:]

    if len(args) > 0:

        if args[0] == 'start':
            from .core.startup import YardbFacade
            yardb_instance = YardbFacade()
            yardb_instance.start()

        if args[0] == 'cli':
            from .core.cli import CLI
            CLI.run()
            return
    else:
        print('Yardb WARNING: you need to pass some argument. See --help.')


if __name__ == '__main__':
    main()