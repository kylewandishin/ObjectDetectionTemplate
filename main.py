from setup import setup
from checkup import checkup
from train import train
from checkVenv import checkVenv

def main():
    checkVenv()
    areWeGood = checkup()
    if areWeGood == 1:
        print("Checkup failed. Please check log for details.")
        exit(1)
    config = setup()
    for model_name in config:
        train(model_name)
if __name__ == "__main__":
    main();
