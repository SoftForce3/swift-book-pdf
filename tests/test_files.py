import pytest
 
from swift_book_pdf.files import find_or_clone_swift_book_repo
 
 
def test_missing_input_directory_has_clear_error_message(tmp_path):
    missing_input_dir = tmp_path / "missing-swift-book"
 
    with pytest.raises(FileNotFoundError) as exc_info:
        find_or_clone_swift_book_repo(
            temp=str(tmp_path),
            input_path=str(missing_input_dir),
        )
 
    message = str(exc_info.value)
 
    assert "Local input directory does not exist" in message
    assert str(missing_input_dir) in message
    assert "--input-path" in message
 
 
def test_input_path_file_has_clear_error_message(tmp_path):
    input_file = tmp_path / "swift-book.txt"
    input_file.write_text("not a directory", encoding="utf-8")
 
    with pytest.raises(NotADirectoryError) as exc_info:
        find_or_clone_swift_book_repo(
            temp=str(tmp_path),
            input_path=str(input_file),
        )
 
    message = str(exc_info.value)
 
    assert "Expected --input-path to point to a directory" in message
    assert str(input_file) in message