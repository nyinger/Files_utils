# file_utils.py

def read_file(file_path):
    """
    Reads the contents of a file.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    str: The contents of the file as a single string.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

def write_to_file(file_path, content):
    """
    Writes content to a file. Overwrites existing content.
    
    Parameters:
    file_path (str): The path to the file.
    content (str): The content to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def append_to_file(file_path, content):
    """
    Appends content to the end of a file.
    
    Parameters:
    file_path (str): The path to the file.
    content (str): The content to append to the file.
    """
    with open(file_path, 'a') as file:
        file.write(content + '\n')
