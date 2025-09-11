'''

This file helps in performing additional tasks on the notebook file, such as finding statistics about the lines/word count.

So, the subject of the tasks done by this file is the existing notebook file in the current folder. 

This file does not have anything to do with data analysis and prediction. It is mostly about notebook file metadata and related tasks.

Statistics such as the total number of Python code lines, number of code and text cells, etc. can be observed by running the file.

'''


import json
import os
import nbformat

def analyze_cells(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    code_cells = [cell for cell in nb.cells if cell.cell_type == 'code']
    markdown_cells = [cell for cell in nb.cells if cell.cell_type == 'markdown']

    print(f"Total cells: {len(nb.cells)}")
    print(f"Code cells: {len(code_cells)}")
    print(f"Markdown cells: {len(markdown_cells)}")

    total_code_lines = sum(len(cell.source.splitlines()) for cell in code_cells)
    print(f"Total lines of code: {total_code_lines}")


def lines_count(path):
    with open(path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    code_lines = 0
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            code_lines += sum(1 for line in cell["source"] if line.strip())  # skip empty lines

    print(f"Total Python code lines: {code_lines}")

    md_lines = 0
    for cell in notebook["cells"]:
        if cell["cell_type"] == "markdown":
            md_lines += sum(1 for line in cell["source"] if line.strip())

    print(f"Total Markdown code lines: {md_lines}")

def extract_clean_code(ipynb_path, output_py_path):
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    with open(output_py_path, 'w', encoding='utf-8') as f_out:
        for i, cell in enumerate(nb.cells):
            if cell.cell_type == 'code':
                lines = cell.source.splitlines()
                clean_lines = [line for line in lines if not line.strip().startswith(('%', '!', '?'))]
                f_out.write(f"# --- Cell {i + 1} ---\n")
                f_out.write('\n'.join(clean_lines) + '\n\n')

# Building the needed paths

# Get directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build path to the input file relative to the script
file_path = os.path.join(script_dir, "house-price-analysis-and-prediction.ipynb")

# Build path for the code extraction output file relative to the script 
python_output_file_path = os.path.join(script_dir, "extracted_code.py")


# Calling functions:

extract_clean_code(file_path, python_output_file_path)

analyze_cells(file_path)

lines_count(file_path)


