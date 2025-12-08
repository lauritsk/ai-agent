import os


def get_files_info(working_directory, directory="."):
    wd_abs_path = os.path.abspath(working_directory)
    dir_abs_path = os.path.join(wd_abs_path, directory)

    if not dir_abs_path.startswith(wd_abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(dir_abs_path):
        return f'Error: "{directory}" is not a directory'

    lines = []
    try:
        for item in os.listdir(dir_abs_path):
            item_path = os.path.join(dir_abs_path, item)
            line = f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            lines.append(line)
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"
