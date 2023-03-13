"""
Update the VMR Excel file
"""

import os
import sys
import argparse
import requests
import re

from .colours import message
from .helper import package_directory

__author__ = 'Rob Edwards'

VMR_URL: str = "https://ictv.global/vmr/current"

def check_new_vmr_available(verbose: bool) -> str:
    """
    Check whether we need to download a new record
    :param verbose: More output
    :return: The name of the current file, or None if we need to download a new file
    """

    r = requests.head(VMR_URL)
    if verbose:
        message(f"Headers downloaded: {r.headers}\n", "BLUE")

    if 'Content-Disposition' not in r.headers:
        message("FATAL: We can't get the filename from the headers. It should be in Content-Disposition", "RED")
        message(f"We have:\n{r.headers}", "RED")
        sys.exit(2)

    filename = re.findall("filename=\"(.+)\"", r.headers['Content-Disposition'])[0]

    if filename and os.path.exists(os.path.join(package_directory, "VMR", filename)):
        return os.path.join(package_directory, "VMR", filename)

    if 'Last-Modified' in r.headers:
        # this is not implemented yet. Basically you need to use datetime to convert the time stamp
        # into unix time and then see if the new file is newer than the old file
        message(f"WARNING: We now have a Last-Modified data in the excel file headers. Tell Rob to fix the code\n",
                "RED")

    return None


def current_vmr(force_download: bool = False, verbose: bool = False) -> str:
    """
    Return the path to the current version of the VMR file
    :param force_download: make me download a new version
    :param verbose: more output
    :return: The name of the current VMR file
    """

    filename = check_new_vmr_available(verbose)
    if not force_download:
        # do we need to download a new file?
        if filename:
            if verbose:
                message("We have the latest VMR", "GREEN")
            return filename

    if filename and os.path.exists(filename):
        if verbose:
            message(f"Removing existing VMR to download a new one: {filename}", "PINK")
        try:
            os.remove(filename)
        except OSError as e:
            message(f"There was an error removing {filename}. Is the file still open in Excel?", "RED")
            message(f"The error was {e.strerror}", "RED")
            sys.exit(2)

    if not os.path.exists(package_directory):
        if verbose:
            message(f"Making a directory for the files in {package_directory}", "BLUE")
        os.makedirs(package_directory, exist_ok=True)

    r = requests.get(VMR_URL)

    if not filename:
        filename = re.findall("filename=\"(.+)\"", r.headers['Content-Disposition'])[0]
        filename = os.path.join(package_directory, "VMR", filename)

    if verbose:
        message(f"Writing to {filename}", "GREEN")
    with open(filename, 'wb') as out:
        out.write(r.content)

    return filename


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download the VMR file')
    parser.add_argument('-f', help='force download', action='store_true')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    current_vmr(args.f, args.v)
