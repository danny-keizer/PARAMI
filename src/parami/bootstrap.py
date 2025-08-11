from pathlib import Path


def bootstrap_directories(dir: str = None) -> None:
    """
    Creates the entire directory structure needed to run the program.

    Args:
        dir (str): The base directory, defaults to /tmp.

    Returns:
        None: ...
    """

    ROOT_DIR = Path(f"/{dir}") / "parami"
    OBJECTS_DIR = ROOT_DIR / "objects"
    ENTRIES_DIR = ROOT_DIR / "objects" / "entries"
    CONSTRAINTS_DIR = ROOT_DIR / "objects" / "constraints"
    FILES_DIR = ROOT_DIR / "objects" / "files"
    DOCS_DIR = ROOT_DIR / "docs"

    for folder in (
        ROOT_DIR,
        OBJECTS_DIR,
        ENTRIES_DIR,
        CONSTRAINTS_DIR,
        FILES_DIR,
        DOCS_DIR,
    ):
        folder.mkdir(0o777, parents=True, exist_ok=True)
