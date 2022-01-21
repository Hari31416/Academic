#!/usr/bin/env python3
import os
import subprocess


def get_output(directory):
    os.chdir(directory)
    with open("geometry.in", "r") as f:
        texts = f.readlines()
        text = texts[-1]
        text = text.split("H")[0].strip()
        print("Distance : " + text[-4:].strip())
    subprocess.run(["extract_output.sh", "output"])
    os.chdir("..")


if __name__ == "__main__":
    output_dirs = os.listdir()
    for dir in output_dirs:
        if "." not in dir:
            try:
                print("Getting output for: " + dir)
                get_output(dir)
            except:
                print(
                    "Error in getting output for: "
                    + dir
                    + "\nProbably it is not a directory."
                )
