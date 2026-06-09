"""Starter code for the Python File Automation assignment."""

from pathlib import Path


def summarize_file(input_path: str) -> dict:
    """Read a text file and return counts for lines, words, and characters."""
    raise NotImplementedError("Implement summarize_file() to count lines, words, and characters.")


def copy_clean_file(input_path: str, output_path: str) -> str:
    """Copy a file while removing blank lines and return the output path."""
    raise NotImplementedError("Implement copy_clean_file() to write cleaned text to the output file.")


def save_report(report: dict, report_path: str) -> None:
    """Write a summary report dictionary to a text file."""
    raise NotImplementedError("Implement save_report() to write report contents to a file.")


if __name__ == "__main__":
    source_file = Path(__file__).parent / "sample_notes.txt"
    cleaned_file = Path(__file__).parent / "clean_notes.txt"
    report_file = Path(__file__).parent / "report.txt"

    print("This starter code provides the file paths for the assignment.")
    print(f"Sample file: {source_file}")
    print(f"Clean file: {cleaned_file}")
    print(f"Report file: {report_file}")
