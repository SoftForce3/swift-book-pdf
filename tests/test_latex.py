from types import SimpleNamespace

from swift_book_pdf.latex import LaTeXConverter


def test_empty_markdown_file_logs_warning(caplog) -> None:
    config = SimpleNamespace(
        assets_dir="assets",
        doc_config=SimpleNamespace(
            mode=None,
            appearance=None,
            font_size=9,
        ),
        font_config=SimpleNamespace(
            main_font="Arial",
        ),
    )

    converter = LaTeXConverter(config)

    with caplog.at_level("WARNING"):
        result = converter.convert_file_to_latex([], "empty-file")

    assert result == []
    assert "Skipping empty markdown file" in caplog.text