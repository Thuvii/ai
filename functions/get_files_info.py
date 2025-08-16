import os

def get_files_info(working_directory, directory="."):
    test_path = os.path.join(working_directory,directory)
    abs_path = os.path.abspath(test_path)
    abs_working_path = os.path.abspath(working_directory)
    if not abs_path.startswith(abs_working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    try:
        list_file = []
        for f in os.listdir(abs_path):
            f_path = os.path.join(abs_path,f)    
            list_file.append(f'{f}: file_size={os.path.getsize(f_path)}, is_dir={os.path.isdir(f_path)}')
        return '\n'.join(list_file)
    except Exception as e:
        return f"Error listing files: {e}"

    