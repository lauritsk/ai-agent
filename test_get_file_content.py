from functions.get_file_content import get_file_content


def test_reads_file_contents(tmp_path):
    file_path = tmp_path / "example.txt"
    file_path.write_text("hello world")

    result = get_file_content(str(tmp_path), "example.txt")

    assert result == "hello world"


def test_rejects_paths_outside_working_directory(tmp_path):
    result = get_file_content(str(tmp_path), "/bin/cat")

    assert (
        result
        == 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory'
    )


def test_reports_missing_files(tmp_path):
    result = get_file_content(str(tmp_path), "missing.txt")

    assert result == 'Error: File not found or is not a regular file: "missing.txt"'


def test_truncates_large_files(tmp_path):
    file_path = tmp_path / "large.txt"
    file_path.write_text("a" * 10001)

    result = get_file_content(str(tmp_path), "large.txt")

    assert len(result) > 10000
    assert result.endswith('[...File "large.txt" truncated at 10000 characters]')
