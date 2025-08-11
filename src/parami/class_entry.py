from mdpython.datautils import jsonutil
from parami.file_operations import *
import pickle
import json
import hashlib
from pathlib import Path
import os


class Entry:
    """Defines the 'Entry' class.

    Entries are created from a data field in a file or an environment variable, the instance represents the data itself as well as it's source.
    Upon creation an entry generates an identifier by hashing some of its own fields.
    Instances are stored as pickles in the 'entries' directory.

    Attributes:
        source    (str): The full path of the instance's pickle file.
        id        (str): The identifier, createn by hashing 'key' and 'value'.
        key       (str): A dot-separated notation of the value's path.
        value     (multiple): Contains the value that was extracted form the source file.
    """

    def __init__(self, source: str, key: str, value):
        """
        Initiate the 'Entry' class.
        """

        self.Source = str(source).split("/")[-1]
        self.Id = self.identifier(key, value)
        self.Key = key
        self.Value = value
        self.save()

    def save(self) -> None:
        """
        Save the 'Entry' instance as a pickle.
        """

        with open(self.path(), "wb") as file:
            pickle.dump(self, file)

    def load(self) -> None:
        """
        Load the 'Entry' instance as a pickle.
        """

        with open(self.path(), "rb") as file:
            return pickle.load(file)

    def delete(self) -> None:
        """
        Delete the 'Entry' instance by removing the pickle.
        """

        os.remove(self.path())

    def path(self) -> None:
        """
        Return the path of the instance pickle.
        """

        return Path(__file__).parent / "inventory" / "objects" / "entries" / f"{self.Id}.pkl"

    def bulk_create_from_json(file: str) -> None:
        """
        Create multiple entries by parsing the fields in a JSON file.
        """

        for key, value in jsonutil.flatten_json(json.loads(read_file(file))).items():
            Entry(source=file, key=key, value=value)

    @staticmethod
    def identifier(x, y) -> hex:
        """
        Create an identifier and return it.
        """

        return hashlib.md5(f"{x}:{y}".encode("utf-8")).hexdigest()
