#!/usr/bin/env python3
import os
import subprocess


def submit():
    runs = os.listdir()
    for run in runs:
        if "." not in run:
            try:
                os.chdir(run)
                subprocess.run(["qsub", "-qlow", "aims_sub.sh"])
                print("Submitted: " + run)
                os.chdir("..")
            except:
                print(
                    "Error in submitting: " + run + "\nProbably it is not a directory."
                )


if __name__ == "__main__":
    submit()
