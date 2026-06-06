from types import SimpleNamespace
from unittest.mock import Mock
 
from swift_book_pdf.book import PDFBookBuilder
 
 
def test_pdf_book_builder_logs_build_summary(caplog) -> None:
    config = SimpleNamespace()
    builder = PDFBookBuilder.__new__(PDFBookBuilder)
    builder.config = config
    builder.summary = Mock()
    builder.summary.format_lines.return_value = [
        "PDF generation completed.",
        "Processed files: 2",
        "Skipped files: 1",
        "Output file: dist/book.pdf",
    ]
 
    with caplog.at_level("INFO"):
        builder._log_build_summary()
 
    assert "PDF generation completed." in caplog.text
    assert "Processed files: 2" in caplog.text
    assert "Skipped files: 1" in caplog.text
    assert "Output file: dist/book.pdf" in caplog.text