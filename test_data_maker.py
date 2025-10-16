import os
from pathlib import Path

# Create test directory
test_dir = Path("test_files")
test_dir.mkdir(exist_ok=True)

# Create some dummy files
test_files = [
    "document1.pdf",
    "report_2023.docx",
    "meeting_notes.txt",
    "presentation_draft.pptx",
    "budget_2023.xlsx"
]

# Create test files with some content
for filename in test_files:
    with open(test_dir / filename, "w") as f:
        f.write(f"Test content for {filename}")

# Create the CSV file
csv_content = """OldFileName,NewFileName
document1.pdf,Final_Report_2025.pdf
report_2023.docx,Annual_Summary.docx
meeting_notes.txt,Team_Meeting_Minutes_Oct.txt
presentation_draft.pptx,Client_Presentation_Final.pptx
budget_2023.xlsx,Financial_Forecast_2025.xlsx"""

with open(test_dir / "rename_mapping.csv", "w") as f:
    f.write(csv_content)

print("Created test files:")
for file in test_files:
    print(f"- {file}")
print("\nCreated rename_mapping.csv")