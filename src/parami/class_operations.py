import pickle
import os
from pathlib import Path


def load_class_instances_from_dir(subdir: str) -> list:
    """
    Loads all of the class instances from pickle files in a given subdirectory.

    Args:
        subdir (str): The subdirectory to scan for instances.

    Returns:
        list: A list of class instance objects.
    """

    batch = []
    items = os.scandir((Path(f"/tmp") / "parami" / "objects" / subdir))
    for item in items:
        if item.is_file():
            with open(item, "rb") as file:
                batch.append(pickle.load(file))

    return batch


def load_class_instance_from_file(subdir: str, name: str) -> object:
    """
    Loads a single class instance from a pickle file in a given subdirectory.

    Args:
        subdir (str): The subdirectory to scan for instances.
        name   (str): The file name of the pickle.

    Returns:
        list: A single class instance object.
    """

    dir = Path(f"/tmp") / "parami" / "objects" / subdir
    with open(f"{dir}/{name}.pkl", "rb") as file:
        return pickle.load(file)


def query_class_instance(search: str, attribute: str, subdir: str = "entries") -> list:
    """
    Builds a list of class object instances from a directory of pickle objects by filtering a given attribute and search string.

    Args:
        subdir      (str): The subdirectory to query for instances.
        attribute   (str): The attribute to match.
        search      (str): A query.

    Returns:
        list: A list of instances that match the query.
    """

    try:
        hits = []
        for instance in load_class_instances_from_dir(subdir=subdir):
            match attribute:

                case "id" | "Id":
                    if search in str(instance.Id) or search in ["all", "All"]:
                        hits.append(instance)

                case "key" | "Key":
                    if search in str(instance.Key) or search in ["all", "All"]:
                        hits.append(instance)

                case "value" | "Value":
                    if search in str(instance.Value) or search in ["all", "All"]:
                        hits.append(instance)

                case "operator" | "Operator":
                    if search in str(instance.Operator) or search in ["all", "All"]:
                        hits.append(instance)

                case "condition" | "Condition":
                    if search in str(instance.Condition) or search in ["all", "All"]:
                        hits.append(instance)

                case "result" | "Result":
                    if search in str(instance.Result) or search in ["all", "All"]:
                        hits.append(instance)

                case _:
                    pass
        return hits

    except FileNotFoundError:
        print("Incorrect Key")
