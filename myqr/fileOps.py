import os


def checkDataDir(dir_str):
    """function to determine whether a data output directory exists.
    if the directory doesn't exist, then it is created"""

    try:
        os.makedirs(dir_str)
        # if DIR doesn't exist, create directory
        return 1

    except OSError:
        return 0


# end of checkDataDir()
