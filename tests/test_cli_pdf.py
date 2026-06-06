from pathlib import Path

import click
import pytest

from swift_book_pdf.cli_pdf import _resolve_pdf_output_path


def test_output_filename_without_extension_adds_pdf_extension() -> None:
    result = _resolve_pdf_output_path("dist", "swift-book")

    assert result == str(Path("dist") / "swift-book.pdf")


def test_output_filename_with_pdf_extension_is_preserved() -> None:
    result = _resolve_pdf_output_path("dist", "swift-book.pdf")

    assert result == str(Path("dist") / "swift-book.pdf")


def test_output_filename_with_invalid_extension_fails() -> None:
    with pytest.raises(click.BadParameter):
        _resolve_pdf_output_path("dist", "swift-book.txt")


def test_output_filename_with_empty_value_fails() -> None:
    with pytest.raises(click.BadParameter):
        _resolve_pdf_output_path("dist", "   ")


def test_output_filename_with_path_fails() -> None:
    with pytest.raises(click.BadParameter):
        _resolve_pdf_output_path("dist", "folder/swift-book.pdf")