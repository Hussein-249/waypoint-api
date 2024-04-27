

def read_csv(filename: str) -> None:
    """Reads a csv file, returns none"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    # with open ensures file will be closed even when exception
    with open(filename, 'w') as f:
        for line in lines:
            # Remove trailing comma and newline
            if line.endswith(",\n"):
                line = line[:-2] + "\n"
            f.write(line)

    return None
