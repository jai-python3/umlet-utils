# -*- coding: utf-8 -*-
import logging
import os
from datetime import datetime
from typing import List

DEFAULT_OUTDIR = os.path.join(
    "/tmp",
    os.path.splitext(os.path.basename(__file__))[0],
    str(datetime.today().strftime("%Y-%m-%d-%H%M%S")),
)

DEFAULT_VERBOSE = False


class Writer:
    """Class for writing the Umlet .uxf files."""

    def __init__(self, **kwargs):
        """Constructor for class for writing the Umlet .uxf files."""
        self.outdir = kwargs.get("outdir", None)
        self.outfile = kwargs.get("outfile", None)
        self.logfile = kwargs.get("logfile", None)
        self.indir = kwargs.get("indir", None)

        logging.info(f"Have instantiated Writer in '{os.path.abspath(__file__)}'")

    def write_file(
        self,
        class_name: str = None,
        private_attributes_list: List[str] = None,
        methods_list: List[str] = None,
    ) -> None:
        """Write the Umlet .uxf file.

        Args:
            class_name (str): the name of the class
            private_attributes_list (list): the list of private attributes declared in the constructor of the class
            methods_list (list): the list of methods defined in the class
        """
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
