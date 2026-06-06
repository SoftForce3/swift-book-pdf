from pathlib import Path

import click


def normalize_pdf_output_filename(output_filename: str) -> str:
    filename = output_filename.strip()

    if not filename:
        raise click.BadParameter(
            "Output filename cannot be empty.",
            param_hint="--output",
        )

    filename_path = Path(filename)

    if filename_path.name != filename:
        raise click.BadParameter(
            "Output filename must be a filename, not a path.",
            param_hint="--output",
        )

    if filename_path.suffix == "":
        filename_path = filename_path.with_suffix(".pdf")
    elif filename_path.suffix.lower() != ".pdf":
        raise click.BadParameter(
            "Output filename must use the .pdf extension.",
            param_hint="--output",
        )

    return filename_path.name