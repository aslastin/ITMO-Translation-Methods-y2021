import argparse
import errno
import os
import subprocess
import sys


def write(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="S@S language compiler")
    parser.add_argument("--path", type=str, help="file with s@s code")
    parser.add_argument("--dir", default=os.getcwd(), type=str,
                        help="output directory, where all c-files will be stored")

    args = parser.parse_args()
    path, directory = args.path, args.dir

    cp = subprocess.run(["cat", path], universal_newlines=True, stdout=subprocess.PIPE)
    cp = subprocess.run(["python", "antlr/main.py"], universal_newlines=True, input=cp.stdout, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    if len(cp.stderr):
        sys.stderr.write(cp.stderr)
        exit(1)

    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    code1_file = f"{directory}/code1.c"
    write(code1_file, cp.stdout)

    cp = subprocess.run(["clang-format", code1_file], universal_newlines=True, stdout=subprocess.PIPE, check=True)

    code2_file = f"{directory}/code2.c"
    write(code2_file, cp.stdout)

    executable_file = f"{directory}/executable"
    subprocess.run(["gcc", "-I", "c-code", "c-code/sasbase.c", code2_file, "-o", executable_file, "-w"])
    subprocess.run([f"./{executable_file}"])
