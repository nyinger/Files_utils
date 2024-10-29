# file_utils.py

def read_file(file_path):
    """
    Reads the contents of a file and returns it as a string.
    
    Parameters:
    file_path (str): Path to the file to be read.
    
    Returns:
    str: Content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return None

def write_to_file(file_path, content):
    """
    Writes content to a file, overwriting if it already exists.
    
    Parameters:
    file_path (str): Path to the file to be written to.
    content (str): Content to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to '{file_path}'.")

def append_to_file(file_path, content):
    """
    Appends content to a file.
    
    Parameters:
    file_path (str): Path to the file to append to.
    content (str): Content to append to the file.
    """
    with open(file_path, 'a') as file:
        file.write(content)
    print(f"Content appended to '{file_path}'.")

def delete_file(file_path):
    """
    Deletes the specified file.
    
    Parameters:
    file_path (str): Path to the file to be deleted.
    """
    import os
    try:
        os.remove(file_path)
        print(f"The file '{file_path}' has been deleted.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")

def file_exists(file_path):
    """
    Checks if the specified file exists.
    
    Parameters:
    file_path (str): Path to the file.
    
    Returns:
    bool: True if the file exists, False otherwise.
    """
    import os
    return os.path.isfile(file_path)
