import os
import sys

def checkVenv():
    if not os.path.exists("venv"):
        print("Virtual environment not found. Please run setup.sh.")
        exit(1)
    