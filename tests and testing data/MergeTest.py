# This script should use a Function to convert a PubMed file to RIS format then merge all ris files together
# The Problem is .txt file from pubmed needs to be converted to .ris file first

import os
import glob
from Bio import Medline
from rispy import BaseWriter


######################################################################################################
# This function converts all PubMed files (ending in .txt) to .ris files.                            
# I want the .ris file to be outputted into the Intput_RIS_files folder for later use of the merge function 
######################################################################################################

def convert_pubmed_to_ris(pubmed_file, ris_file):
    # glob.glob(os.path.join(pubmed_dir, '*.txt')): This line is supposed to find all the .txt files 
    # in a folder named pubmed_dir (which represents the directory where your PubMed files are). 
    # The *.txt part is like saying "find everything that ends with .txt".
    pubmed_files = glob.glob(os.path.join(r'C:\Users\georg\Documents\Python_Scripts\RIS_file_concat\Input_RIS_files', '*.txt'))

    # This line starts a loop. For each .txt file found in the folder, the loop will do something with that file.
    for pubmed_file in pubmed_files:
        # Parse the PubMed file
        # with open(pubmed_file) as handle: This opens each .txt file one by one.
        # records = Medline.parse(handle): Reads the content of the file and organizes it into a format (called records) that the program can work with.
        with open(pubmed_file) as handle:
            records = Medline.parse(handle)

        # Create the corresponding RIS file name. These lines create the name for the new RIS file based on the original PubMed file's name.
        # This line generates the path for the new RIS file. It combines the directory path, created by replacing the .txt extension of the PubMed file with .ris.
        base_name = os.path.basename(pubmed_file)
        ris_file = os.path.join(r'C:\Users\georg\Documents\Python_Scripts\RIS_file_concat\Input_RIS_files', '*.txt', os.path.splitext(base_name)[0] + '.ris')

        # Write the data to an RIS file
        # with open(ris_file, 'w') as outfile: This creates a new RIS file to write into.
        # writer = BaseWriter(outfile): This sets up a tool (writer) to write into the RIS file.
        # for record in records:: For each piece of data in the PubMed file, it's converted 
        # into a format suitable for the RIS file and then written into that file.
        with open(ris_file, 'w') as outfile:
            writer = BaseWriter(outfile)
            for record in records:
                # Convert the PubMed record to an RIS record
                ris_record = {
                    'TY': record.get('PT', ''), # Publication Types
                    'AN': record.get('PMID', ''),  # PubMed ID
                    'TI': record.get('TI', ''),  # Title
                    'AU': record.get('AU', []),  # List of authors [multiple entries]
                    'PY': record.get('DP', ''),  # Date of publication
                    'AB': record.get('AB', ''),  # Abstract
                    'AD': record.get('AD', []),  # Affiliation [multiple entries]
                    'JI': record.get('AB', ''),  # Journal name
                    'VL': record.get('VI', ''),  # Volume number
                    'IS': record.get('IP', ''),  # Issue number
                    'DO': record.get('AID', ''),  # DOI (Digital Object Identifier)                      
                    'T2': record.get('SO', ''),  # Source (Journal)
                    'JF': record.get('JT', ''),# Journal Title
                    'JO': record.get('TA', ''),  # Journal Abbreviation
                    'DA': record.get('DEP', ''),  # Date of Electronic Publication
                    'SP': record.get('PG', ''),  # Start Page                           
                    'KW': record.get('MH', []),  # Keywords [multiple entries]
                    'C1': record.get('AD', ''),  # Author Address
                    'LA': record.get('LA', ''),  # Language
                    'ID': record.get('AID', ''), # Article Identifier
                    'SN': record.get('IS', ''),  # ISSN                
                }
                writer.write(ris_record)
    

pubmed_directory = r'C:\Users\georg\Documents\Python_Scripts\RIS_file_concat\Input_RIS_files'
ris_directory = r'C:\Users\georg\Documents\Python_Scripts\RIS_file_concat\input_RIS_files'
convert_pubmed_to_ris(pubmed_directory, ris_directory)




###########################################################################################
# DONT TOUCH CODE: This merges the ris file together and works fine. Dont touch this code #
###########################################################################################
        
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
output_file = r'C:\Users\georg\Documents\Python_Scripts\RIS_file_concat\Output_RIS_files'


#############################################################################
# Call the function to merge RIS files (and convert PubMed files if present)#
#############################################################################

merge_ris_files_in_folder(folder_path, output_file)

print("SUCCESS, well done snippy")

import webbrowser
# URL to open to the dedupe.nl page
url = 'http://dedupendnote.nl/'
# Open URL in a new tab of the default web browser
webbrowser.open_new_tab(url)