# -*- coding: utf-8 -*-
import logging
import os
from datetime import datetime
from typing import Any, Dict, List

DEFAULT_OUTDIR = os.path.join(
    "/tmp",
    os.path.splitext(os.path.basename(__file__))[0],
    str(datetime.today().strftime("%Y-%m-%d-%H%M%S")),
)

DEFAULT_VERBOSE = False


X_INITIAL_POSITION = 100
Y_INITIAL_POSITION = 500

WIDTH = 200
HEIGHT = 150

X_POSITION_INCREMENT = 10
Y_POSITION_INCREMENT = 10

ZOOM_LEVEL = 10

BACKGROUND_COLOR = "green"


class Writer:
    """Class for writing the Umlet .uxf files."""

    def __init__(self, **kwargs):
        """Constructor for class for writing the Umlet .uxf files."""
        self.outdir = kwargs.get("outdir", None)
        self.outfile = kwargs.get("outfile", None)
        self.logfile = kwargs.get("logfile", None)
        self.indir = kwargs.get("indir", None)
        self.verbose = kwargs.get("verbose", None)

        logging.info(f"Have instantiated Writer in '{os.path.abspath(__file__)}'")

    def write_file(self, file_objects: List[Dict[Any, Any]]) -> None:
        """Write the Umlet .uxf file.

        Args:
            file_objects (list): list of dictionaries containing the following:
                class_name (str): the name of the class
                private_attributes_list (list): the list of private attributes declared in the constructor of the class
                methods_list (list): the list of methods defined in the class
        """
        x = X_INITIAL_POSITION
        y = Y_INITIAL_POSITION
        w = WIDTH
        h = HEIGHT
        zoom_level = ZOOM_LEVEL
        background_color = BACKGROUND_COLOR

        content = []

        content.append('<diagram program="umletino" version="15.0.0">')
        content.append(f"<zoom_level>{zoom_level}</zoom_level>")

        for obj in file_objects:
            class_name = obj["class_name"]
            while class_name.endswith(":"):
                class_name = class_name.rstrip(":")

            methods_list = obj["methods_list"]
            private_attributes_list = obj["private_attributes_list"]
            logging.info(
                f"Here are the '{len(private_attributes_list)} private attributes declared in the constructor of class '{class_name}'"
            )
            for attribute in private_attributes_list:
                logging.info(attribute)

            logging.info(
                f"Here are the '{len(methods_list)}' methods declared in the class '{class_name}'"
            )
            for method in methods_list:
                logging.info(method)

            content.append(
                f"""<element>
                        <id>UMLClass</id>
                        <coordinates>
                            <x>{x}</x>
                            <y>{y}</y>
                            <w>{w}</w>
                            <h>{h}</h>
                        </coordinates>
                        <panel_attributes>bg={background_color}"""
            )
            content.append(class_name)
            content.append("--")

            for attribute in private_attributes_list:
                content.append(f"- {attribute}")

            content.append("--")

            for method in methods_list:
                if method.startswith("_"):
                    content.append(f"- {method}")
                else:
                    content.append(f"+ {method}")
            content.append(
                """</panel_attributes>
                    <additional_attributes></additional_attributes>
                </element>"""
            )

            x += X_POSITION_INCREMENT
            y += Y_POSITION_INCREMENT

        content.append("</diagram>")

        with open(self.outfile, "w") as of:
            for line in content:
                of.write(f"{line}\n")

        logging.info(f"Wrote file '{self.outfile}'")
        if self.verbose:
            print(f"Wrote file '{self.outfile}'")
