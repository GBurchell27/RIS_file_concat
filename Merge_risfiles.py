import os

def merge_ris_files_in_folder(folder_path, output_file):
    merged_content = ""
    for filename in os.listdir(folder_path):
        if filename.endswith('.ris'):
            file_path = os.path.join(folder_path, filename)
            try:
                # Specify encoding as 'utf-8'
                with open(file_path, 'r', encoding='utf-8') as file:
                    merged_content += file.read() + "\n"
            except UnicodeDecodeError:
                # If utf-8 doesn't work, try 'latin-1' which is more permissive
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        merged_content += file.read() + "\n"
                except IOError as e:
                    print(f"Error reading file {file_path} with latin-1 encoding: {e}")
            except IOError as e:
                print(f"Error reading file {file_path} with utf-8 encoding: {e}")

    try:
        # Write to a specific output path
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(merged_content)
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

# Set the folder containing RIS and PubMed files
folder_path = r'C:\Users\georg\Documents\Python_Scripts\RIS_file_concat\Input_RIS_files'

# Set the full path for the output file
output_file = r'C:\Users\georg\Documents\Python_Scripts\RIS_file_concat\Output_RIS_files\merged.ris'

# Call the function to merge RIS files
merge_ris_files_in_folder(folder_path, output_file)

print("SUCCESS, well done")


############################################
# This opens new webpage to dedupendnote.nl# 
import webbrowser
# URL to open to the dedupe.nl page
url = 'http://dedupendnote.nl/'
# Open URL in a new tab of the default web browser
webbrowser.open_new_tab(url)
