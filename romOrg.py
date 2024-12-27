import os
import shutil
import re
import argparse

region_patterns = {
    'USA': [r'(U|USA)'],
    'Japan': [r'(J|Japan)'],
    'Europe': [r'(E|Europe)'],
    'Korea': [r'(K|Korea)'],
    'Unknown': [r'(Unknown)'],
    'Other': []  # This will be the default category for unmatched ROMs
}

# parse command-line arguments.
def parse_arguments():
    parser = argparse.ArgumentParser(description='Organize ROM files into folders by region and alphabet.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input folder containing ROMs.')
    parser.add_argument('-o', '--output', required=True, help='Path to the output folder for organized ROMs.')
    args = parser.parse_args()
    return args.input, args.output

# region-finding time
def get_region(filename):
    # find all parentheses
    matches = re.findall(r'\((.*?)\)', filename)

    # if no parentheses, go to the shadow realm.
    if not matches:
        return 'Other'

    for match in matches:
        match = match.strip()

        for region, patterns in region_patterns.items():
            for pattern in patterns:
                # check if pattern matches the region name, case-insensitive
                if re.search(pattern, match, re.IGNORECASE):
                    return region

    # if no region is found:
    return 'Other'

# handle special characters and numbers (mostly numbers)
def get_special_characters_folder(rom_file):
    if rom_file[0].isdigit():
        return '1'  # Folder for numbers
    elif not rom_file[0].isalnum():
        return '2'  # Folder for special characters
    return None

# let us organize now
def organize_roms(input_path, output_path):
    for console in os.listdir(input_path):
        console_path = os.path.join(input_path, console)

        if not os.path.isdir(console_path):
            continue  # skip non-directories

        for rom_file in os.listdir(console_path):
            rom_path = os.path.join(console_path, rom_file)

            if os.path.isfile(rom_path):
                # check for special characters or numbers
                special_folder = get_special_characters_folder(rom_file)
                if special_folder:
                    print(f"Checking {rom_file}... Found special category '{special_folder}', organizing by region.")
                    
                    # determine region first
                    region = get_region(rom_file)
                    region_folder = os.path.join(output_path, console, region)
                    os.makedirs(region_folder, exist_ok=True)
                    
                    # Place into the corresponding special folder under the region
                    special_folder_path = os.path.join(region_folder, special_folder)
                    os.makedirs(special_folder_path, exist_ok=True)
                    
                    # copy into the appropriate folder
                    shutil.copy(rom_path, os.path.join(special_folder_path, rom_file))
                    continue  # Skip further processing

                # otherwise, continue
                region = get_region(rom_file)

                print(f"Checking {rom_file}... Found region {region}, moving to {region}")
                
                # create the region folder if it doesn't exist
                region_folder = os.path.join(output_path, console, region)
                os.makedirs(region_folder, exist_ok=True)

                # first letter of the ROM file for alphabetical sorting
                first_letter = rom_file[0].upper()
                
                # create a folder for the first letter if it doesn't exist
                letter_folder = os.path.join(region_folder, first_letter)
                os.makedirs(letter_folder, exist_ok=True)

                # copy the file into the correct folder
                shutil.copy(rom_path, os.path.join(letter_folder, rom_file))

def main():
    try:
        # arguments
        input_path, output_path = parse_arguments()

        # input path exists?
        if not os.path.exists(input_path):
            print(f"Error: Input path '{input_path}' does not exist.")
            return
        
        # output path exists? if not, create it
        if not os.path.exists(output_path):
            print(f"Output path '{output_path}' does not exist. Creating it now.")
            os.makedirs(output_path)

        organize_roms(input_path, output_path)
        print("ROMs have been successfully organized.")
        # input("Press Enter to finish.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Usage: python organize_roms.py -i <input_path> -o <output_path>")

if __name__ == '__main__':
    main()
