"""
Author: Wade Wang
Date: 06/12/2025
Description: Week3 - Activity2 Develop an OOP-based solution to continue W3-A1 by adding an "End of File" message to your project. Once completed, Share your updated code.
"""

from pathlib import Path


class FileReader:
    def __init__(self, filename: str):
        # Always load the file next to this script so cwd does not matter
        self.file_path = Path(__file__).with_name(filename)
        self.content = self.file_path.read_text(encoding="utf-8")

    def print_content(self) -> None:
        # Output the file text
        print(self.content)

    def count_stars(self) -> None:
        # Print how many '*' characters
        print(f"Number of '*' characters: {self.content.count('*')}")

    def append_content(self, message: str) -> None:
        # Append a message to the content
        self.content += f"\n{message}"

if __name__ == "__main__":
    file_reader = FileReader("demo_file.txt")
    file_reader.append_content("End of File")
    file_reader.print_content()
