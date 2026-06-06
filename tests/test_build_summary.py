from pathlib import Path
 
from swift_book_pdf.build_summary import BuildSummary
 
def test_build_summary_starts_with_zero_counts() -> None:
    summary = BuildSummary()
    assert summary.processed_files == 0
    assert summary.skipped_files == 0
    assert summary.output_path is None
 
 
def test_build_summary_counts_processed_and_skipped_files() -> None:
    summary = BuildSummary()
    summary.mark_processed()
    summary.mark_processed()
    summary.mark_skipped()
    assert summary.processed_files == 2
    assert summary.skipped_files == 1
 
 
def test_build_summary_formats_final_pdf_message() -> None:
    summary = BuildSummary()
    summary.mark_processed()
    summary.mark_skipped()
    summary.set_output_path("dist/book.pdf")
    assert summary.format_lines() == [
        "PDF generation completed.",
        "Processed files: 1",
        "Skipped files: 1",
        f"Output file: {Path('dist/book.pdf')}",
    ]
 