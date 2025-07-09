def count_words_in_file(filepath):
    """
    Reads a text file, counts the number of words in it, and handles errors gracefully.

    Args:
        filepath (str): Path to the text file.

    Returns:
        int: Number of words in the file, or -1 if an error occurs.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            return len(content.split())
    except FileNotFoundError:
        print(f"[Error] File not found: '{filepath}'")
        return -1
    except Exception as e:
        print(f"[Error] An unexpected error occurred while reading '{filepath}': {e}")
        return -1


def create_sample_file():
    """
    Creates a sample text file named 'sample.txt' for testing purposes.
    """
    try:
        with open("sample.txt", "w", encoding="utf-8") as f:
            f.write("This is a sample text file.\n")
            f.write("It has a few words.\n")
            f.write("New lines count as spaces.")
        print("[Info] 'sample.txt' created successfully.")
    except Exception as e:
        print(f"[Error] Could not create 'sample.txt': {e}")


def run_tests():
    """
    Runs word count tests on existing, newly created, and non-existent files.
    """
    print("=== Word Count Test ===")

    # Create a sample file
    create_sample_file()

    # List of test files
    test_files = ["sample.txt", "word_counter/my_file.txt", "non_existent_file.txt"]

    for file in test_files:
        print(f"\nTesting file: {file}")
        count = count_words_in_file(file)
        if count != -1:
            print(f"[Success] '{file}' contains {count} words.")
        else:
            print(f"[Failed] Could not count words in '{file}'.")

    print("\n=== Test Complete ===")


if __name__ == "__main__":
    run_tests()

