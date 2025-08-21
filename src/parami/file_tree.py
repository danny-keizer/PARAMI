from pathlib import Path


def bootstrap_directories() -> None:
    """
    Creates the entire directory structure needed to run the program.

    Args:
        dir (str): The base directory.

    Returns:
        None: ...
    """

    IVENTORY_DIR    = Path(__file__).parent / "inventory"
    LOGS_DIR        = IVENTORY_DIR / "logs"
    DOCS_DIR        = IVENTORY_DIR / "docs"
    OBJECTS_DIR     = IVENTORY_DIR / "objects"
    ENTRIES_DIR     = OBJECTS_DIR / "entries"
    CONSTRAINTS_DIR = OBJECTS_DIR / "constraints"
    FILES_DIR       = OBJECTS_DIR / "entries"

    for folder in (
        IVENTORY_DIR,
        LOGS_DIR,
        OBJECTS_DIR,
        ENTRIES_DIR,
        CONSTRAINTS_DIR,
        FILES_DIR,
        DOCS_DIR,
    ):
        folder.mkdir(0o777, parents=True, exist_ok=True)
    
    return f"Init succesful, logging will be directed to: {LOGS_DIR}"
