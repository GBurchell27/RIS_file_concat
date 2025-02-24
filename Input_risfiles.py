# Workflow goes as follows:
    # Collect all ris files from independant databases (must be .ris files)

    # **WINDOWS+R** Write: "Input_risfiles"
    # This will open a folder where you can place all the RIS files you want to merge
    # Copy all the RIS files you want to merge into the folder "Input_RIS_files"

    # **WINDOWS+R** Write: "Merge_risfile"
    # This will merge all the RIS files into a single file in the folder "Output_RIS_files"
    # Merged file can now be put into dedupe.nl for deduplication



import os
import subprocess

def open_folder(path):
    """
    Opens the folder at the specified path.
    """
    if os.path.exists(path):
        # For Windows
        subprocess.run(['explorer', path])
        # For MacOS, uncomment the line below and comment out the Windows line
        # subprocess.run(['open', path])
        # For Linux, uncomment the line below and comment out the Windows line
        # subprocess.run(['xdg-open', path])
    else:
        print(f"Folder not found: {path}")

# Example usage
folder_path = r'C:\Users\georg\Documents\Python_Scripts\RIS_file_concat'  # Replace with your folder path
open_folder(folder_path)

print('Workflow goes as follows:')
print('1) Preparation:')
print('- Collect all ris files from independant databases (PubmMed, Embase ect), they need to be .ris files to work')
print(' ')
print('2) Input your .ris files into a single foler:')
print('- **WINDOWS+R** Write: "Input_risfiles" - Well done you have reached this far')
print('- Copy all the RIS files you want to merge into the folder "Input_RIS_files"')
print(' ')
print('3) Merge your .ris files:')
print('- **WINDOWS+R** Write: "Merge_risfile"')
print('- The merged ris file will be found in the "output_RIS_files" ')
print('- dedupeendnote.nl should automatically open where the ris file can be placed')