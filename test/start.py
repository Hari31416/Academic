#!/usr/bin/env python3
import shutil
import os
import subprocess


def create_files(n, m):
    new_dir = "run" + str(n)
    shutil.copytree("run1", new_dir, symlinks=False, ignore=None)
    os.chdir(new_dir)
    with open("geometry.in", "r") as f:
        text = f.read()
        text_new = text.replace("1", str(m))
        with open("geometry.in", "w") as f:
            f.write(text_new)
    os.chdir("..")


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
    values = [
        # 1.0,
        # 0.9,
        # 0.85,
        # 0.8,
        # 0.7,
        # 0.6,
        # 0.5,
        # 0.71,
        # 0.72,
        # 0.73,
        # 0.74,
        # 0.75,
        # 0.76,
        # 0.77,
        0.78,
        0.79,
    ]
    for i in range(len(values)):
        j = i + 2
        to_path = "run" + str(j)
        if os.path.exists(to_path):
            shutil.rmtree(to_path)

        print("Creating run" + str(j))
        print(f"Changing 1 to {values[i]}")
        create_files(j, values[i])

    submit()
    print("Done")
    print("Here are all the submitted jobs.")
    subprocess.run(["qstat", "-u", "$USER"])
