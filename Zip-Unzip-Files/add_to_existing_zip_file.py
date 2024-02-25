import zipfile

def add_to_zip(zip_filename, file_to_add):
    with zipfile.ZipFile(zip_filename, 'a') as zip:
        zip.write(file_to_add)

# Usage
add_to_zip('dfs.zip', 'file_to_add.txt')
