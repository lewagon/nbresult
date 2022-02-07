
from wagon_common.helpers.scope import resolve_scope

import pickle


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

    print(pickles)
