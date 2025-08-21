import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_path_test = os.path.abspath(os.path.join(working_directory, file_path))
    abs_path_working = os.path.abspath(working_directory)
    if not abs_path_test.startswith(abs_path_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
    if not os.path.exists(abs_path_test):
        return f'Error: File "{file_path}" not found.' 
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        new_list = ["python", abs_path_test]
        if args:
            new_list.extend(args)
        res = subprocess.run(new_list,timeout=30,capture_output=True,cwd=abs_path_working,text=True)
        output = []
        if res.stdout:
            output.append(f'STDOUT: {res.stdout}')
        if res.stderr:
            output.append(f'STDERR: {res.stderr}')
        if res.returncode != 0:
            output.append(f'Processed exited with code {res.returncode}')
        if not output:
            return "No output produced"
        return '\n'.join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute file specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file."  
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
    ),
)