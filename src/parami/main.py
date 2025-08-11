from parami.dispatch import *
from parami.bootstrap import *
from parami.class_constraint import *
from parami.class_entry import *
from parami.class_operations import *
from parami.file_operations import *
from parami.rich_visuals import *
from rich.console import Console
import argparse
import os


def main():

    """
    The main entry for the program, takes commands and arguments through argparse.

    Args:
        None: ...

    Returns:
        None: ...
    """

    # "MAIN" PARSER
    parser = argparse.ArgumentParser(description=f"Parami CLI")
    crud_subparsers = parser.add_subparsers(dest="command", required=True)

    # "CREATE" SUBPARSER
    create_parser = crud_subparsers.add_parser("create", help="Create an object")
    create_sub = create_parser.add_subparsers(dest="target", required=True)

    # "READ" SUBPARSER
    read_parser = crud_subparsers.add_parser("read", help="Read an object")
    read_sub = read_parser.add_subparsers(dest="target", required=True)

    # "UPDATE" SUBPARSER
    update_parser = crud_subparsers.add_parser("update", help="Update an object")
    update_sub = update_parser.add_subparsers(dest="target", required=True)

    # "DELETE" SUBPARSER
    delete_parser = crud_subparsers.add_parser("delete", help="Delete an object")
    delete_sub = delete_parser.add_subparsers(dest="target", required=True)

    # "APPLY" SUBPARSER
    apply_parser = crud_subparsers.add_parser("apply", help="Apply an object")
    apply_sub = apply_parser.add_subparsers(dest="target", required=True)

    # "CREATE" TARGETS
    create_entry = create_sub.add_parser(
        "entry", help="Create an object of type Entry()"
    )
    create_entry.add_argument("--file", "-f", help="entry name")
    create_entry.add_argument("--env", help="entry name")

    create_constraint = create_sub.add_parser(
        "constraint", help="Create an object of type Constraint()"
    )
    create_constraint.add_argument("key", help="constraint key")
    create_constraint.add_argument("operator", help="constraint operator")
    create_constraint.add_argument("condition", help="constraint condition")

    # "READ" TARGETS
    read_entry = read_sub.add_parser("entry", help="Read an object of type Entry()")
    read_entry.add_argument("--attribute", "-a", required=True, help="entry name")
    read_entry.add_argument("--search", "-s", required=True, help="entry name")

    read_constraint = read_sub.add_parser(
        "constraint", help="Read an object of type Constraint()"
    )
    read_constraint.add_argument(
        "--attribute", "-a", required=True, help="constraint name"
    )
    read_constraint.add_argument(
        "--search", "-s", required=True, help="constraint name"
    )

    # "UPDATE" TARGETS
    update_entry = update_sub.add_parser(
        "entry", help="Update an object of type Entry()"
    )
    update_entry.add_argument("--attribute", "-a", required=True, help="entry name")
    update_entry.add_argument("--search", "-s", required=True, help="entry name")
    update_entry.add_argument("--key", "-k", required=False, help="entry name")
    update_entry.add_argument("--value", "-v", required=False, help="entry name")

    update_constraint = update_sub.add_parser(
        "constraint", help="Update an object of type Constraint()"
    )
    update_constraint.add_argument(
        "--attribute", "-a", required=True, help="constraint name"
    )
    update_constraint.add_argument(
        "--search", "-s", required=True, help="constraint name"
    )
    update_constraint.add_argument(
        "--condition", "-c", required=False, help="constraint name"
    )

    # "DELETE" TARGETS
    delete_entry = delete_sub.add_parser(
        "entry", help="Delete an object of type Entry()"
    )
    delete_entry.add_argument("--attribute", "-a", required=True, help="entry name")
    delete_entry.add_argument("--search", "-s", required=True, help="entry name")

    delete_constraint = delete_sub.add_parser(
        "constraint", help="Delete an object of type Constraint()"
    )
    delete_constraint.add_argument(
        "--attribute", "-a", required=True, help="constraint name"
    )
    delete_constraint.add_argument(
        "--search", "-s", required=True, help="constraint name"
    )

    # "APPLY" TARGETS
    apply_policy = apply_sub.add_parser("policy", help="Apply a Policy")
    apply_policy.add_argument("--file", help="policy name")

    args = parser.parse_args()

    match args.command:
        case "create":
            match args.target:
                case "entry":
                    dispatch_create_entry(file=args.file, env=args.env)

                case "constraint":
                    dispatch_create_constraint(
                        key=args.key, operator=args.operator, condition=args.condition
                    )

        case "read":
            match args.target:
                case "entry":
                    dispatch_read_entry(attribute=args.attribute, search=args.search)

                case "constraint":
                    dispatch_read_constraint(
                        attribute=args.attribute, search=args.search
                    )

        case "update":
            match args.target:
                case "entry":
                    dispatch_update_entry(
                        attribute=args.attribute,
                        search=args.search,
                        set_key=args.key,
                        set_value=args.value,
                    )

                case "constraint":
                    dispatch_update_constraint(
                        attribute=args.attribute,
                        search=args.search,
                        set_condition=args.condition,
                    )

        case "delete":
            match args.target:
                case "entry":
                    dispatch_delete_entry(attribute=args.attribute, search=args.search)

                case "constraint":
                    dispatch_delete_constraint(
                        attribute=args.attribute, search=args.search
                    )

        case "apply":
            match args.target:
                case "policy":
                    dispatch_apply_policy(file=args.file)

        case _:
            console.print(f"Unknown command: {args.command}")


if __name__ == "__main__":
    bootstrap_directories("tmp")
    console = Console()
    os.system("cls||clear")
    main()
