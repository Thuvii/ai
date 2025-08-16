import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_path_test = os.path.abspath(os.path.join(working_directory, file_path))
    abs_path_working = os.path.abspath(working_directory)
    if not abs_path_test.startswith(abs_path_working):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path_test):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_path_test, "r") as f:
            file_content = f.read(MAX_CHARS + 1)
            if len(file_content) > MAX_CHARS:
                return f'{file_content} "{file_path}" truncated at {MAX_CHARS} characters'
            return f'- {file_path.upper()}:\n{file_content}'
    except Exception as e:
         return f"Error listing files: {e}"
        
    