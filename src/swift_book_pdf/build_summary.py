from dataclasses import dataclass
from pathlib import Path
 
 
@dataclass
class BuildSummary:
    processed_files: int = 0
    skipped_files: int = 0
    output_path: str | None = None
 
    def mark_processed(self) -> None:
        self.processed_files += 1
 
    def mark_skipped(self) -> None:
        self.skipped_files += 1
 
    def set_output_path(self, output_path: str) -> None:
        self.output_path = str(Path(output_path))
 
    def format_lines(self) -> list[str]:
        output_file = self.output_path or "unknown"
 
        return [
            "PDF generation completed.",
            f"Processed files: {self.processed_files}",
            f"Skipped files: {self.skipped_files}",
            f"Output file: {output_file}",
        ]
    