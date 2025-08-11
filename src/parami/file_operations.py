import json
import yaml
import xmltodict
import hcl2
import toml
from pathlib import Path


def read_file(filename: str) -> None:
    """
    Reads a file with utf-8 encoding and returns the contents.

    Args:
        filename (str): Name of the file.

    Returns:
        None: I/O Stream.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_file(filename: str, content) -> None:
    """
    Writes a file with utf-8 encoding and returns the contents.

    Args:
        filename (str): Name of the file.
        content  (str): Contents to write to the file.

    Returns:
        None: I/O Stream.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(content)


def convert_yaml_to_json(infile: str) -> None:
    """
    Reads a YAML file and converts it to JSON, then returns the destination path.

    Args:
        infile (str): Name of the file that will be converted.

    Returns:
        None: I/O Stream.
    """
    data = yaml.safe_load(read_file(infile))
    outfile = Path(f"/tmp") / "parami" / "objects" / "files" / infile
    write_file(filename=outfile, content=json.dumps(data, indent=2))
    return outfile


def convert_xml_to_json(infile: str) -> None:
    """
    Reads an XML file and converts it to JSON, then returns the destination path.

    Args:
        infile (str): Name of the file that will be converted.

    Returns:
        None: I/O Stream.
    """
    data = xmltodict.parse(read_file(infile))
    outfile = Path(f"/tmp") / "parami" / "objects" / "files" / infile
    write_file(filename=outfile, content=json.dumps(data, indent=2))
    return outfile


def convert_toml_to_json(infile: str) -> None:
    """
    Reads a TOML file and converts it to JSON, then returns the destination path.

    Args:
        infile (str): Name of the file that will be converted.

    Returns:
        None: I/O Stream.
    """
    data = toml.load(infile)
    outfile = Path(f"/tmp") / "parami" / "objects" / "files" / infile
    write_file(filename=outfile, content=json.dumps(data, indent=2))
    return outfile


def convert_tfvars_to_json(infile: str) -> None:
    """
    Reads a HCL file and converts it to JSON, then returns the destination path.

    Args:
        infile (str): Name of the file that will be converted.

    Returns:
        None: I/O Stream.
    """
    outfile = Path(f"/tmp") / "parami" / "objects" / "files" / infile
    with open(infile, "r") as file:
        data = hcl2.load(file)
        write_file(filename=outfile, content=json.dumps(data, indent=2))
    return outfile
