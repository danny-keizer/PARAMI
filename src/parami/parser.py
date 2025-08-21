from rich.console import Console
from rich.table import Table
from parami.file_operations import *
from parami.class_operations import *
from parami.rich_visuals import *
from parami.class_entry import *
from parami.class_constraint import *
import subprocess
import os


@log
def parse_create_entry(
    args_type_file:   str | None = None,
    args_type_env:    str | None = None,
    args_type_manual: str | None = None,
    ):

    if args_type_file:
        extension = args_type_file.split(".")
        match extension[-1]:
            case "json":
                Entry.bulk_create_from_json(args_type_file)

            case "yaml" | "yml":
                Entry.bulk_create_from_json(convert_yaml_to_json(infile=args_type_file))

            case "xml":
                Entry.bulk_create_from_json(convert_xml_to_json(infile=args_type_file))

            case "tfvars" | "tf":
                Entry.bulk_create_from_json(convert_tfvars_to_json(infile=args_type_file))

            case "toml":
                Entry.bulk_create_from_json(convert_toml_to_json(infile=args_type_file))

            case _:
                console.print("Unsupported file type")

    if args_type_env and os.getenv(args_type_env):
        Entry(source=".env", 
              key=args_type_env, 
              value=os.getenv(args_type_env))

        return

    if args_type_manual:
        pass


@log
def parse_read_entry(
    args_search_all:    str | None = None,
    args_search_search: str | None = None,
    args_attribute:     str | None = None,
    ):

    if args_search_all:
        generate_table_from_list_of_class(title="Entries", lst=query_class_instance(attribute="id", search="all", subdir="entries"), type="entry")

    elif args_search_search and not args_attribute:
        generate_table_from_list_of_class(title="Entries", lst=query_class_instance(attribute="id", search=args_search_search, subdir="entries"), type="entry")

    elif args_search_search and args_attribute:
        generate_table_from_list_of_class(title="Entries", lst=query_class_instance(attribute=args_attribute, search=args_search_search, subdir="entries"), type="entry")   


@log
def parse_update_entry(
    args_search_all:    str | None = None,
    args_search_search: str | None = None,
    args_attribute:     str | None = None,
    args_key:           str | None = None,
    args_value:         str | None = None,
    ):

    if args_search_all:
        for entry in query_class_instance(attribute="id", search="all", subdir="entries"):
            if args_key: entry.Key = args_key
            elif args_value: entry.Value = args_value
            entry.save()


    elif args_search_search and not args_attribute:
        for entry in query_class_instance(attribute="id", search=args_search_search, subdir="entries"):
            if args_key: entry.Key = args_key
            elif args_value: entry.Value = args_value
            entry.save()

    elif args_search_search and args_attribute:
        for entry in query_class_instance(attribute=args_attribute, search=args_search_search, subdir="entries"):
            if args_key: entry.Key = args_key
            elif args_value: entry.Value = args_value     
            entry.save()


@log
def parse_delete_entry(
    args_search_all:    str | None = None,
    args_search_search: str | None = None,
    args_attribute:     str | None = None,
    ):

    if args_search_all:
        for entry in query_class_instance(attribute="id", search="all", subdir="entries"):
            entry.delete()

    elif args_search_search and not args_attribute:
        for entry in query_class_instance(attribute="id", search=args_search_search, subdir="entries"):
            entry.delete()

    elif args_search_search and args_attribute:
        for entry in query_class_instance(attribute=args_attribute, search=args_search_search, subdir="entries"):
            entry.delete()


@log
def parse_create_constraint(
    args_scope:     str | None = None,
    args_operator:  str | None = None,
    args_condition: str | None = None,
    ):

    for constraint in query_class_instance(attribute="key", search=args_scope, subdir="entries"):
        Constraint(
            id=constraint.Id,
            key=constraint.Key,
            value=constraint.Value,
            operator=args_operator,
            condition=args_condition,
        )


@log
def parse_read_constraint(
    args_search_all:    str | None = None,
    args_search_search: str | None = None,
    args_attribute:     str | None = None,
    ):

    if args_search_all:
        generate_table_from_list_of_class(title="Constraints", lst=query_class_instance(attribute="id", search="all", subdir="constraints"), type="constraint")

    elif args_search_search and not args_attribute:
        generate_table_from_list_of_class(title="Constraints", lst=query_class_instance(attribute="id", search=args_search_search, subdir="constraints"), type="constraint")

    elif args_search_search and args_attribute:
        generate_table_from_list_of_class(title="Constraints", lst=query_class_instance(attribute=args_attribute, search=args_search_search, subdir="constraints"), type="constraint")


@log
def parse_update_constraint(
    args_search_all:    str | None = None,
    args_search_search: str | None = None,
    args_attribute:     str | None = None,
    args_condition:     str | None = None,
    ):

    if args_search_all:
        for constraint in query_class_instance(attribute="id", search="all", subdir="constraints"):
            constraint.Condition = args_condition
            constraint.Result = constraint.test()
            constraint.save()

    elif args_search_search and not args_attribute:
        for constraint in query_class_instance(attribute="id", search=args_search_search, subdir="constraints"):
            constraint.Condition = args_condition
            constraint.Result = constraint.test()
            constraint.save()

    elif args_search_search and args_attribute:
        for constraint in query_class_instance(attribute=args_attribute, search=args_search_search, subdir="constraints"):
            constraint.Condition = args_condition
            constraint.Result = constraint.test()
            constraint.save()


@log
def parse_delete_constraint(
    args_search_all:    str | None = None,
    args_search_search: str | None = None,
    args_attribute:     str | None = None,
    ):

    if args_search_all:
        for constraint in query_class_instance(attribute="id", search="all", subdir="constraints"):
            constraint.delete()

    elif args_search_search and not args_attribute:
        for constraint in query_class_instance(attribute="id", search=args_search_search, subdir="constraints"):
            constraint.delete()

    elif args_search_search and args_attribute:
        for constraint in query_class_instance(attribute=args_attribute, search=args_search_search, subdir="constraints"):
            constraint.delete()

def parse_apply_policy(file: str):
    subprocess.run(f"./{file}")