# -*- coding: utf-8 -*-
import logging
import os
from datetime import datetime

DEFAULT_OUTDIR = os.path.join(
    "/tmp",
    os.path.splitext(os.path.basename(__file__))[0],
    str(datetime.today().strftime("%Y-%m-%d-%H%M%S")),
)

DEFAULT_VERBOSE = False


class Parser:
    """Class for parsing Python .py files."""

    def __init__(self, **kwargs):
        """Constructor for class for parsing Python .py files."""

        self.infile = kwargs.get("infile", None)

        self.is_parsed = False
        self.private_attributes_list = []
        self.class_name = None
        self.methods_list = []

        logging.info(f"Have instantiated Parser in '{os.path.abspath(__file__)}'")

    def get_private_attributes_list(self) -> None:
        """Retrieve the list of private attributes declared in the constructor
        of the class.

        Returns:
            list: list of private attributes
        """
        if not self.is_parsed:
            self._parse_file()
        return self.private_attributes_list

    def get_class_name(self) -> None:
        """Retrieve the name of the class.

        Returns:
            str: name of the class
        """
        if not self.is_parsed:
            self._parse_file()
        return self.class_name

    def get_methods_list(self) -> None:
        """Retrieve the list of method names defined in the class.

        Returns:
            list: list of method names
        """
        if not self.is_parsed:
            self._parse_file()
        return self.methods_list

    def _parse_file(self) -> None:
        logging.info(f"Will read file '{self.infile}'")
        line_ctr = 0
        found_constructor = False
        processed_constructor = False
        with open(self.infile, "r") as f:
            for line in f:
                line_ctr += 1
                line = line.strip()

                if line.startswith("class "):
                    class_name = line.replace("class ", "")
                    if "(" in class_name:
                        parts = class_name.split("(")
                        class_name = parts[0]
                    self.class_name = class_name
                elif line.startswith("def __init__(self"):
                    found_constructor = True

                elif found_constructor and not processed_constructor:
                    if line.startswith("self."):
                        private_attribute = (
                            line.lstrip("self.").split("=")[0].replace(" ", "")
                        )
                        logging.info(
                            f"derived private attribute '{private_attribute}' from line '{line}'"
                        )
                        self.private_attributes_list.append(private_attribute)
                    elif line.startswith("def "):
                        processed_constructor = True
                        found_constructor = False
                        method = line.lstrip("def ").split("(")[0]
                        logging.info(f"derived method '{method}' from line '{line}'")
                        self.methods_list.append(method)

                elif line.startswith("def ") and processed_constructor:
                    method = line.lstrip("def ").split("(")[0]
                    logging.info(f"derived method '{method}' from line '{line}'")
                    self.methods_list.append(method)

        if line_ctr > 0:
            logging.info(f"Read '{line_ctr}' lines from file '{self.infile}'")
        else:
            logging.info(f"Did not read any lines from file '{self.infile}'")
        self.is_parsed = True
