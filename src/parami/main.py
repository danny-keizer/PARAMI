from rich.console import Console
from rich.markdown import Markdown
from parami.parser import *
from parami.file_tree import *
from parami.class_constraint import *
from parami.class_entry import *
from parami.class_operations import *
from parami.file_operations import *
from parami.rich_visuals import *
import argparse
import os


def main():

    """
    The main entry point for the program.

    Args:
        None: ...

    Returns:
        None: ...
    """


    # MAIN PARSER
    parser = argparse.ArgumentParser(description=f"Parami CLI")
    crud_subparsers = parser.add_subparsers(dest="command", required=True)


    # CREATE SUBPARSER
    create_parser = crud_subparsers.add_parser("create", help="Create an object")
    create_sub = create_parser.add_subparsers(dest="target", required=True)


    # READ SUBPARSER
    read_parser = crud_subparsers.add_parser("read", help="Read an object")
    read_sub = read_parser.add_subparsers(dest="target", required=True)


    # UPDATE SUBPARSER
    update_parser = crud_subparsers.add_parser("update", help="Update an object")
    update_sub = update_parser.add_subparsers(dest="target", required=True)


    # DELETE SUBPARSER
    delete_parser = crud_subparsers.add_parser("delete", help="Delete an object")
    delete_sub = delete_parser.add_subparsers(dest="target", required=True)

    # INIT SUBPARSER
    crud_subparsers.add_parser("init", help="Initialize the program")

    # APPLY SUBPARSER
    apply_parser = crud_subparsers.add_parser("apply", help="Apply something")
    apply_sub = apply_parser.add_subparsers(dest="target", required=True)

    # CREATE ENTRY
    create_entry = create_sub.add_parser("entry", help="entry")
    create_entry_group_type = create_entry.add_mutually_exclusive_group(required=True)

    create_entry_group_type.add_argument("--file", help="expects a path or filename")
    create_entry_group_type.add_argument("--env", help="expects the name of an environment variable")
    create_entry_group_type.add_argument("--manual", help="expects key='value' ")

    # READ ENTRY
    read_entry = read_sub.add_parser("entry", help="entry")
    read_entry_group_search = read_entry.add_mutually_exclusive_group(required=True)

    read_entry_group_search.add_argument("--all", action="store_true", help="all objects of this type")
    read_entry_group_search.add_argument("--search", help="all matching objects")

    read_entry.add_argument("--attribute", help="the attribute to search")

    # UPDATE ENTRY
    update_entry = update_sub.add_parser("entry", help="entry")
    update_entry_group_search = update_entry.add_mutually_exclusive_group(required=True)
    update_entry_group_kv = update_entry.add_mutually_exclusive_group(required=True)

    update_entry_group_search.add_argument("--all", action="store_true", help="all objects of this type")
    update_entry_group_search.add_argument("--search", help="all matching objects")

    update_entry_group_kv.add_argument("--key", help="value to replace the key with")
    update_entry_group_kv.add_argument("--value", help="value to replace the value with")

    update_entry.add_argument("--attribute", help="the attribute to search")

    # DELETE ENTRY
    delete_entry = delete_sub.add_parser("entry", help="entry")
    delete_entry_group_search = delete_entry.add_mutually_exclusive_group(required=True)

    delete_entry_group_search.add_argument("--all", action="store_true", help="all objects of this type")
    delete_entry_group_search.add_argument("--search", help="all matching objects")

    delete_entry.add_argument("--attribute", help="the attribute to search")

    # CREATE CONSTRAINT
    create_constraint = create_sub.add_parser("constraint", help="constraint")

    create_constraint.add_argument("scope", help="constraint scope")
    create_constraint.add_argument("operator", help="constraint operator")
    create_constraint.add_argument("condition", help="constraint condition")

    # READ CONSTRAINT
    read_constraint = read_sub.add_parser("constraint", help="constraint")
    read_constraint_group_search = read_constraint.add_mutually_exclusive_group(required=True)

    read_constraint_group_search.add_argument("--all", action="store_true", help="all objects of this type")
    read_constraint_group_search.add_argument("--search", help="all matching objects")

    read_constraint.add_argument("--attribute", help="the attribute to search")

    # UPDATE CONSTRAINT
    update_constraint = update_sub.add_parser("constraint", help="constraint")
    update_constraint_group_search = update_constraint.add_mutually_exclusive_group(required=True)

    update_constraint_group_search.add_argument("--all", action="store_true", help="all objects of this type")
    update_constraint_group_search.add_argument("--search", help="all matching objects")

    update_constraint.add_argument("--attribute", help="the attribute to search")
    update_constraint.add_argument("--condition", help="the condition to modify", required=True)

    # DELETE CONSTRAINT
    delete_constraint = delete_sub.add_parser("constraint", help="constraint")
    delete_constraint_group_search = delete_constraint.add_mutually_exclusive_group(required=True)

    delete_constraint_group_search.add_argument("--all", action="store_true", help="all objects of this type")
    delete_constraint_group_search.add_argument("--search", help="all matching objects")

    delete_constraint.add_argument("--attribute", help="the attribute to search")

    # APPLY FILE
    apply_policy = apply_sub.add_parser("policy", help="Apply a Policy")
    apply_policy.add_argument("--file", help="the file name", required=True)

    args = parser.parse_args()
    logger.info(f"Issued CLI Command {args}")


    match args.command:
            case "create":
                match args.target:
                    case "entry":
                        parse_create_entry(args_type_file=args.file, args_type_env=args.env, args_type_manual=args.manual)

                    case "constraint":
                        parse_create_constraint(args_scope=args.scope, args_operator=args.operator, args_condition=args.condition)

            case "read":
                match args.target:
                    case "entry":
                        parse_read_entry(args_search_all=args.all, args_search_search=args.search, args_attribute=args.attribute) 

                    case "constraint":
                        parse_read_constraint(args_search_all=args.all, args_search_search=args.search, args_attribute=args.attribute)

            case "update":
                match args.target:
                    case "entry":
                        parse_update_entry(args_search_all=args.all, args_search_search=args.search, args_attribute=args.attribute, args_key=args.key, args_value=args.value)

                    case "constraint":
                        parse_update_constraint(args_search_all=args.all, args_search_search=args.search, args_attribute=args.attribute, args_condition=args.condition)

            case "delete":
                match args.target:
                    case "entry":
                        parse_delete_entry(args_search_all=args.all, args_search_search=args.search, args_attribute=args.attribute)   

                    case "constraint":
                        parse_delete_constraint(args_search_all=args.all, args_search_search=args.search, args_attribute=args.attribute)  

            case "init":
                console.print(bootstrap_directories(), style="green")

            case "apply":
                match args.target:
                    case "policy":
                        parse_apply_policy(file=args.file)

            case _:
                console.print(f"Unknown command: {args.command}")

    logger.info(f"Exited CLI Command {args}")


if __name__ == "__main__":
    main()
