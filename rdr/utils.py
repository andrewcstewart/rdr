from pathlib import Path

def search_upwards_for_file(filename):
    """Search in the current directory and all directories above it 
    for a file of a particular name.

    Arguments:
    ---------
    filename :: string, the filename to look for.

    Returns
    -------
    pathlib.Path, the location of the first file found or
    None, if none was found
    """
    d = Path.cwd()
    root = Path(d.root)

    while d != root:
        attempt = d / filename
        if attempt.exists():
            return attempt
        d = d.parent

    return None
