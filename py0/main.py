import os
import sys
import subprocess
from .transpiler import transpile_file

def main():
    if len(sys.argv) != 2:
        print("Usage: py0 <filename.py0>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not input_file.endswith('.py0'):
        print("Error: Input file must have .py0 extension")
        sys.exit(1)

    dir_path = os.path.dirname(os.path.abspath(input_file))
    for file in os.listdir(dir_path):
        if file.endswith('.py0'):
            py0_file = os.path.join(dir_path, file)
            py_file = py0_file[:-4] + '.py'
            transpile_file(py0_file, py_file)
            print(f"Transpiled {py0_file} to {py_file}")

    output_file = input_file[:-4] + '.py'
    subprocess.run(['python', output_file])

if __name__ == '__main__':
    main()