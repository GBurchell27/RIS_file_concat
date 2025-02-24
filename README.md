# RIS File Merger Tool

A Python-based utility for merging multiple RIS (Research Information Systems) files from different academic databases into a single file for systematic reviews.

## Overview

This tool simplifies the process of combining RIS files from various academic databases (PubMed, Embase, Web of Science, Cochrane, Scopus, etc.) into a single merged file for deduplication. The workflow is streamlined into three simple steps using Windows shortcuts.

## Features

- Merges multiple RIS files into a single output file
- Supports both UTF-8 and Latin-1 encodings
- Handles RIS files from all major academic databases
- Automatic redirection to dedupendnote.nl for deduplication
- Simple Windows shortcut-based workflow

## Prerequisites

- Python 3.x installed
- Windows operating system
- RIS files from your database searches

## Installation

1. Clone or download this repository
2. Ensure all files are in the same directory structure:
   ```
   RIS_file_concat/
   ├── Input_RIS_files/
   ├── Output_RIS_files/
   ├── Merge_risfiles.py
   ├── Input_risfiles.py
   ├── Merge_risfiles.bat
   ├── Input_risfiles.bat
   ```

## Usage

The workflow consists of three simple steps:

### 1. Prepare Your RIS Files
- Export RIS files from your chosen academic databases
- Ensure all files have the `.ris` extension

### 2. Input Files (Windows+R: "Input_risfiles")
- Press `Windows+R`
- Type `Input_risfiles`
- Copy all your RIS files into the opened `Input_RIS_files` folder

### 3. Merge Files (Windows+R: "Merge_risfile")
- Press `Windows+R`
- Type `Merge_risfile`
- The tool will:
  - Merge all RIS files from the input folder
  - Save the merged file in `Output_RIS_files`
  - Automatically open dedupendnote.nl in your default browser

## File Structure

- `Input_RIS_files/`: Place your RIS files here
- `Output_RIS_files/`: Contains the merged output file
- `Merge_risfiles.py`: Main merging script
- `Input_risfiles.py`: File management script
- `Merge_risfiles.bat`: Windows shortcut for merging
- `Input_risfiles.bat`: Windows shortcut for input folder

## Error Handling

The tool includes robust error handling for:
- File encoding issues (supports both UTF-8 and Latin-1)
- File reading/writing errors
- Invalid file formats

## Contributing

Feel free to submit issues and enhancement requests.

## License

[Your chosen license]

## Acknowledgments

- dedupendnote.nl for providing deduplication services
