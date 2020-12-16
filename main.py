import random, sys
from glob import glob
from cmd import Cmd
from src import core
# internal modules in use


def main():

    core.banner()
    print("Version: {}".format(core.grap_version))
    core.show_help_menu()
    menu_running = 1
    while[menu_running == 1]:
        try:
            take_input = input('prompt:').lower()
            if take_input == "help":
                print("This is a quick help in args usage ")
            if take_input == "banner":
                core.banner()
            if take_input == "help" or take_input == "?" or take_input == "h":
                core.show_help_menu()
            if take_input == "exit" or take_input == "q" or take_input == "quit":
                sys.exit()

            else:
                pass
        except KeyboardInterrupt:
            print("\nTo hell with this place, I'm out...")
            sys.exit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Danger Will Robinson:, {e}")
