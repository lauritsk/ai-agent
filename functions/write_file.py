import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    wd_abs_path = os.path.abspath(working_directory)
    file_abs_path = os.path.abspath(os.path.join(wd_abs_path, file_path))

    if not file_abs_path.startswith(wd_abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(file_abs_path), exist_ok=True)
        with open(file_abs_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {e}"
