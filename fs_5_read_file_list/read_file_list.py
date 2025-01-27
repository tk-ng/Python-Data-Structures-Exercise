def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

    f = open(filename,"r")
    context = f.read()
    context_list = context.splitlines()
    print('\n'.join([f"- {c}" for c in context_list]))

    # with open(filename) as f:
    #     for line in f:
    #         # remove newline at end of line!
    #         line = line.strip()
    #         print(f"- {line}")

