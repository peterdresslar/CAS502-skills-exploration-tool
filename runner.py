# just a simple runner for skills.py

import subprocess
import sys


def main():
    subprocess.run([sys.executable, "skills.py"]) # note this will ONLY work if skills.py stays where it is now in the project root

if __name__ == "__main__":
    main()