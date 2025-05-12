def build_url(base_url, path):
    return f"{base_url.rstrip('/')}/{path.lstrip('/')}"

def create_general_keys_file(input_string):
    """
    Creates or overwrites a general_keys.txt file in the main directory with the given input string.
    
    Args:
        input_string (str): The string to write to the file
        
    Returns:
        bool: True if successful, False if there was an error
    """
    try:
        # Write to general_keys.txt in the main directory
        with open('general_keys.txt', 'w') as f:
            f.write(input_string)
        return True
    except Exception as e:
        print(f"Error writing to general_keys.txt: {str(e)}")
        return False