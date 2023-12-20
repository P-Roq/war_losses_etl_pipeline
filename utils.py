import os
import sys


def get_parent_directory(depth: int, insert_path: bool) -> str:
    current_directory = os.getcwd()

    # Split the directory path into individual components
    components = current_directory.split(os.sep)
    
    total_components = len(components)

    if depth > total_components:
        raise Exception(f'The number of child folders to skip ({depth}) cannot be equal or superior to the total number of folders in the directory ({total_components}).')

    # Calculate the new path based on the specified depth
    new_path = os.sep.join(components[:-depth] if depth > 0 else components)

    if insert_path:
        sys.path.insert(0, new_path)

    if (total_components - depth) == 1:
        return '/'
    else:
        return new_path
    




