from rich.console import Console
from rich.table import Table
from parami.file_operations import *
from parami.class_operations import *
from parami.rich_visuals import *
from parami.class_entry import *
from parami.class_constraint import *
import subprocess
import os


def dispatch_create_entry(file: str, env: str = None):

    if env != None and os.getenv(env) != None:
        Entry(source=".env", key=env, value=os.getenv(env))
        return

    if file != None:
        extension = file.split(".")
        match extension[-1]:
            case "json":
                Entry.bulk_create_from_json(file)

            case "yaml" | "yml":
                Entry.bulk_create_from_json(convert_yaml_to_json(infile=file))

            case "xml":
                Entry.bulk_create_from_json(convert_xml_to_json(infile=file))

            case "tfvars" | "tf":
                Entry.bulk_create_from_json(convert_tfvars_to_json(infile=file))

            case "toml":
                Entry.bulk_create_from_json(convert_toml_to_json(infile=file))

            case _:
                console.print("Unsupported file type")


def dispatch_read_entry(
    attribute: str = "id", search: str = "all", subdir: str = "entries"
):
    generate_table_from_list_of_class(
        title="Entries",
        lst=query_class_instance(attribute=attribute, search=search, subdir=subdir),
        type="entry",
    )


def dispatch_update_entry(
    set_key: str,
    set_value,
    attribute: str = "id",
    search: str = "all",
    subdir: str = "entries",
):
    for entry in query_class_instance(
        attribute=attribute, search=search, subdir=subdir
    ):
        if set_key != None:
            entry.Key = set_key
        if set_value != None:
            entry.Value = set_value
        entry.save()
    dispatch_read_entry()


def dispatch_delete_entry(
    attribute: str = "id", search: str = "all", subdir: str = "entries"
):
    for entry in query_class_instance(
        attribute=attribute, search=search, subdir=subdir
    ):
        entry.delete()


def dispatch_create_constraint(key: str, operator: str, condition: str | int | float):
    for entry in query_class_instance(attribute="key", search=key, subdir="entries"):
        Constraint(
            id=entry.Id,
            key=entry.Key,
            value=entry.Value,
            operator=operator,
            condition=condition,
        )


def dispatch_read_constraint(
    attribute: str = "id", search: str = "all", subdir: str = "constraints"
):
    generate_table_from_list_of_class(
        title="Constraints",
        lst=query_class_instance(attribute=attribute, search=search, subdir=subdir),
        type="constraint",
    )


def dispatch_update_constraint(
    set_condition: str,
    attribute: str = "id",
    search: str = "all",
    subdir: str = "constraints",
):
    for constraint in query_class_instance(
        attribute=attribute, search=search, subdir=subdir
    ):
        if set_condition != None:
            constraint.Condition = set_condition
        constraint.Result = constraint.test()
        constraint.save()


def dispatch_delete_constraint(
    attribute: str = "id", search: str = "all", subdir: str = "constraints"
):
    for constraint in query_class_instance(
        attribute=attribute, search=search, subdir=subdir
    ):
        constraint.delete()


def dispatch_apply_policy(file: str):
    subprocess.run(f"./{file}")
    dispatch_read_constraint()


console = Console()
