import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory {path} not found.")
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            files.extend(find_files(suffix, item_path))
        elif os.path.isfile(item_path) and item.endswith(suffix):
            files.append(item_path)
    return files


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2: Empty Directory
    print("\nTest Case 2: Empty directory")
    result = find_files(".c", "./emptydir")  # Create first an empty directory with the emptydir name
    print(result)
    # Expected output: []

    # Test Case 3: No files matching the suffix
    print("\nTest Case 3: No matching files")
    result = find_files(".py", "./testdir")
    print(result)
    # Expected output: []

    # Test Case 4: Directory does not exist
    print("\nTest Case 4: Non-existent directory")
    try:
        result = find_files(".c", "./nonexistentdir")
        print(result)
    except FileNotFoundError as e:
        print("Caught error:", e)
    # Expected output: Caught error: [Errno 2] No such file or directory: './nonexistentdir'

    # Test Case 5: Search for files with no extension
    print("\nTest Case 5: Searching for files with no extension")
    result = find_files("", "./testdir")
    print(result)
    # Expected output: List with all files in the directory

    # Test Case 6: search for files with long extension
    print("\nTest Case 6: Searching for specific file type")
    result = find_files(".cpp", "./testdir")
    print(result)
