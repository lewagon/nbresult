
from wagon_common.helpers.scope import resolve_scope


def run_check(sources, verbose):
    """
    iterate through pickle files in the scope
    list pickle files data types
    """

    print("run check")

    # retrieve git controlled files in scope
    controlled_files = resolve_scope(sources, ["*.pickle"], verbose=verbose)[0]

    print(controlled_files)
