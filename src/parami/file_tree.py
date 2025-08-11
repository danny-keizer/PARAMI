from pathlib import Path


def bootstrap_directories() -> None:
    """
    Creates the entire directory structure needed to run the program.

    Args:
        dir (str): The base directory, defaults to /tmp.

    Returns:
        None: ...
    """

    IVENTORY_DIR    = Path(__file__).parent / "inventory"
    DOCS_DIR        = IVENTORY_DIR / "docs"
    OBJECTS_DIR     = IVENTORY_DIR / "objects"
    ENTRIES_DIR     = OBJECTS_DIR / "entries"
    CONSTRAINTS_DIR = OBJECTS_DIR / "constraints"
    FILES_DIR       = OBJECTS_DIR / "entries"

    for folder in (
        IVENTORY_DIR,
        OBJECTS_DIR,
        ENTRIES_DIR,
        CONSTRAINTS_DIR,
        FILES_DIR,
        DOCS_DIR,
    ):
        folder.mkdir(0o777, parents=True, exist_ok=True)
