import os

def write_file(working_directory, file_path, content):
    abs_path_test = os.path.abspath(os.path.join(working_directory, file_path))
    abs_path_working = os.path.abspath(working_directory)
    mkdir_name = os.path.dirname(abs_path_test)
    if not abs_path_test.startswith(abs_path_working):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(mkdir_name):
        try:
            os.mkdir(mkdir_name)
        except Exception as e:
            return f'Error: creating directory: {e}'
    if os.path.exists(abs_path_test) and os.path.isdir(abs_path_test):
        return f'Error: "{file_path}" is a directory not a file'
    try:
        with open(abs_path_test, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"
            
            