import os
import subprocess


def clone_core_algo():
    os.chdir('./core')
    subprocess.run(['git', 'clone', 'git@github.com:UTP-project/core-algo.git'])

def main():
    clone_core_algo()

if __name__ == "__main__":
    main()