
from wagon_common.helpers.scope import resolve_scope

import pickle

import warnings

from colorama import Fore, Style


# TBC: avoid pickle data types warning
warnings.filterwarnings("ignore", category=UserWarning)


def run_check(sources, verbose):
    """
    iterate through pickle files in the scope
    list pickle files data types
    """

    print("run check")

    # retrieve git controlled files in scope
    controlled_files = resolve_scope(sources, ["*.pickle"], verbose=verbose)[0]

    pickles = dict()

    # iterate through files
    for pickle_file in controlled_files:

        # load pickle
        with open(pickle_file, "rb") as file:

            # retrieve content
            content = pickle.load(file)

            # iterate through instance variables
            for key, value in content.__dict__.items():

                data_type = type(value).__name__
                if data_type not in pickles:
                    pickles[data_type] = dict()

                if pickle_file not in pickles[data_type]:
                    pickles[data_type][pickle_file] = []

                pickles[data_type][pickle_file].append(key)

    # show results
    print(Fore.BLUE
          + "\nPickles containing:"
          + Style.RESET_ALL)

    for data_type, pickle_files in pickles.items():

        print(f"- {data_type}: {sum([len(v) for k, v in pickle_files.items()])}")

    # show detailed results
    for data_type, pickle_files in pickles.items():

        print(Fore.BLUE
              + f"\nPickles containing {data_type}:"
              + Style.RESET_ALL)

        for pickle_file, attributes in pickle_files.items():

            print(f"- {pickle_file}: ", end="")

            print(Fore.GREEN
                  + f"({', '.join(attributes)})"
                  + Style.RESET_ALL)
