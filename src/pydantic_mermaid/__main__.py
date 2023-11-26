import argparse
import importlib
import logging
import os
import sys
from importlib.util import module_from_spec, spec_from_file_location
from types import ModuleType
from uuid import uuid4

from pydantic_mermaid.mermaid_generator import MermaidGenerator
from pydantic_mermaid.models import Relations

logger = logging.getLogger("pydantic-mermaid")


def import_module(path: str) -> ModuleType:
    """
    Helper which allows modules to be specified by either dotted path notation or by filepath.
    If we import by filepath, we must also assign a name to it and add it to sys.modules BEFORE
    calling 'spec.loader.exec_module' because there is code in pydantic which requires that the
    definition exist in sys.modules under that name.
    """
    try:
        if os.path.exists(path):
            name = uuid4().hex
            spec = spec_from_file_location(name, path, submodule_search_locations=[])
            module = module_from_spec(spec)  # type: ignore
            sys.modules[name] = module
            spec.loader.exec_module(module)  # type: ignore
            return module
        else:
            return importlib.import_module(path)
    except Exception as e:  # pragma: no cover
        logger.error("The --module argument must be a module path separated by dots or a valid filepath")
        raise e


def _parse_cli_args() -> argparse.Namespace:
    """
    Parses the command-line arguments passed to pydantic-mermaid.
    """
    parser = argparse.ArgumentParser(
        prog="pydantic-mermaid",
        description=main.__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-m",
        "--module",
        type=str,
        help="name or filepath of the python module.\n" "Discoverable submodules will also be checked.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="name of the file the mermaid chart should be written to.",
    )
    parser.add_argument(
        "-n",
        "--root",
        type=str,
        help="Root node for dependency chart or inheritance chart",
        default="",
    )
    parser.add_argument(
        "-e",
        "--relations",
        nargs="+",
        type=str,
        help="Dependency or Inheritance chart",
        default="dependency",
    )
    return parser.parse_args()


def main():
    """
    CLI entrypoint
    """
    args = _parse_cli_args()
    module_type = import_module(args.module)

    mg = MermaidGenerator(module_type)
    relations = Relations.Dependency
    if "dependency" in args.relations and "inheritance" in args.relations:
        relations = Relations.Dependency | Relations.Inheritance
    elif "dependency" in args.relations:
        relations = Relations.Dependency
    elif "inheritance" in args.relations:
        relations = Relations.Inheritance

    chart_content = mg.generate_chart(root=args.root, relations=relations)
    with open(args.output, "w") as f:
        f.write(chart_content)


if __name__ == "__main__":  # pragma: no cover
    main()
