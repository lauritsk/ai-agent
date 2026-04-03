from functions.get_files_info import get_files_info


def test_lists_directory_contents(tmp_path):
    nested_dir = tmp_path / "pkg"
    nested_dir.mkdir()
    file_path = tmp_path / "notes.txt"
    file_path.write_text("hello")

    result = get_files_info(str(tmp_path), ".")

    assert "- notes.txt: file_size=5 bytes, is_dir=False" in result
    assert "- pkg: file_size=" in result
    assert "is_dir=True" in result


def test_rejects_paths_outside_working_directory(tmp_path):
    result = get_files_info(str(tmp_path), "../")

    assert "is_dir=" in result


def test_reports_non_directory_paths(tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("hello")

    result = get_files_info(str(tmp_path), "notes.txt")

    assert result == 'Error: "notes.txt" is not a directory'
