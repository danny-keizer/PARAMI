from rich.console import Console
from rich.table import Table


def generate_table_from_list_of_class(title: str, lst: list, type: str) -> Table:
    """
    Creates and populates a table dynamically from a last of class object instances by indexing their respective keys and values.

    Args:
        title (str): Name of the file that will be converted.
        lst   (list): A list of class object instances.
        type  (type): A label respresenting the class object, used to apply the appropriate styling.
    Returns:
        Table: A complete table.
    """

    try:
        table = Table(
            title=title,
            style="black",
        )
        keys = list(lst[0].__dict__.keys())

        for item in keys:
            table.add_column(str(item), justify="left", style="white")

        for item in lst:
            row = [str(getattr(item, key, "")) for key in keys]

            match type:
                case "constraint":
                    table.add_row(
                        *row,
                        style=(
                            "yellow"
                            if item.Result in [None, "Invalid"]
                            else ("green" if item.Result else "red")
                        ),
                    )

                case "entry":
                    table.add_row(*row, style="white")

                case _:
                    table.add_row(*row, style="white")

        console.print(table)

    except IndexError:
        console.print("[PRM701]: NoInstancesOfObjectTypeWereFound", style="red")

    except TypeError:
        console.print("[PRM702]: DoesNotExist", style="red")


console = Console()
