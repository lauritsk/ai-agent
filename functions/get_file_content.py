import os

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    wd_abs_path = os.path.abspath(working_directory)
    file_abs_path = os.path.abspath(os.path.join(wd_abs_path, file_path))

    if not file_abs_path.startswith(wd_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(file_abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(file_abs_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            extra = f.read(1)
            if extra:
                file_content_string += (
                    f'[...File "{file_path}" truncated at 10000 characters]'
                )
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
