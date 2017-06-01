
import os

print(os.path.exists('/tmp/exist-file'))

print(os.path.exists('/tmp/not-exist-file'))

import pathlib

p = pathlib.Path.home() / '.ssh' / 'config'     # $HOME/.ssh/config
print(p.exists())

print(p.is_file())
print(p.is_dir())

