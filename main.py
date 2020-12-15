import random
from cmd import Cmd

# internal modules in use
from modules_repo.ascii_banners import import_banner





def banner():
    # verbose initalize the module
    b = import_banner
    # show random ascii art as header
    print(b.art[random.randint(0, len(b.art) - 1)])


def main():
    class MyPromt(Cmd):
        prompt = 'Reap Souls'
        intro = banner()

        def do_exit(self, inp):
            '''exit the application.'''
            print("R.I.P application")
            return True


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Danger Will Robinson:, {e}")