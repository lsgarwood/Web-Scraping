import sys

if __name__ == "__AccessingCLArgs/main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

        # run python AccessingCLArgs/main.py Python Command Line Arguments