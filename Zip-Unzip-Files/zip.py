
import os
import zipfile

def zip_files_in_directory(source_directory, target_zip_file_path):
    # Create a ZipFile Object
    with zipfile.ZipFile(target_zip_file_path, 'w') as zip_file:
        # Iterate over all the files in directory
        for foldername, subfolders, filenames in os.walk(source_directory):
            for filename in filenames:
                # Create complete filepath of file in directory
                filePath = os.path.join(foldername, filename)
                # Add file to zip without path
                zip_file.write(filePath, arcname=filename)

# Usage
                
# for example
# zip_files_in_directory('C:/Users/HP/Desktop/fake', 'C:/Users/HP/Desktop/your_zip_file.zip') # use forward slash (/) or double backslash (\\)

zip_files_in_directory('source_directory', 'target_directory/your_zip_file.zip')
