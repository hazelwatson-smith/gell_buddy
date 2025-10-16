# File Renamer 🥺

A simple GUI application that renames files in a directory based on mappings provided in a CSV file.

## Features
- User-friendly graphical interface
- CSV-based file renaming
- Live status updates
- Error handling and validation

## Requirements
- Python 3.6+
- Windows (tested on Windows 10/11)

## Installation

1. Clone the repository:
```powershell
git clone <repository-url>
cd gell_buddy
```

2. (Optional) Create and activate a virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

## Running as Python Script

1. Run the script:
```powershell
python FileRenamer.py
```

## Creating an Executable

1. Install PyInstaller:
```powershell
pip install pyinstaller
```

2. Create the executable:
```powershell
pyinstaller --onefile --windowed --add-data "uwu.png;." FileRenamer.py
```

The executable will be created in the `dist` folder.

## Usage

1. Launch the application (either `FileRenamer.py` or the executable)
2. Click "Browse" to select your CSV file
3. Click "Browse" to select the directory containing files to rename
4. Click "Rename Files" to start the process

### CSV Format
Your CSV file should have this structure:
```csv
OldFileName,NewFileName
document1.pdf,Final_Report_2025.pdf
report_2023.docx,Annual_Summary.docx
```

### Test Files
To create test files for trying out the application:
1. Run `create_test_files.py`
2. Use the generated `test_files` folder and `rename_mapping.csv`

## Troubleshooting

- If the icon doesn't appear, ensure `uwu.png` is in the same directory as the script/executable
- Make sure your CSV has the correct column headers: `OldFileName` and `NewFileName`
- Check file permissions if renaming fails
- Files must exist in the selected directory with exact names as in CSV

## License
MIT License

## Authors
Jordan RJ (JNR1) & Hazel WS 