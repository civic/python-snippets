import subprocess
import sys

if sys.version_info[0] >= 3:
    subprocess.run(["ls", "-l"])
else:
    subprocess.call(["ls", "-l"])
