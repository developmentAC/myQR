import os


def check_data_dir(dir_str: str) -> bool:
    """Ensure an output directory exists.

    Returns True if the directory was created, False if it already existed.
    """

    try:
        os.makedirs(dir_str)
        return True

    except OSError:
        return False


def checkDataDir(dir_str: str) -> bool:
    """Backward-compatible wrapper for older teaching materials."""
    return check_data_dir(dir_str)


# end of check_data_dir()
