import sys

filepath= "foo/bar/filename.txt"

if sys.version_info[0:2] >= (3,5):
    import pathlib

    p = pathlib.Path(filepath)
    p.parent.mkdir(parents=True, exist_ok=True)

else:
    import os
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)





