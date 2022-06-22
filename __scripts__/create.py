import os
import sys
from shutil import copytree

from utils.colors import green, red

baseDir: str = os.getcwd()
patternName: str = sys.argv[1] if len(sys.argv) > 1 else "ADD_NAME_HERE"

print('using template at: {}/../__template__'.format(baseDir))
print('cloning into: {}/../{}'.format(baseDir, patternName))

try:
    copytree('{}/../__template__'.format(baseDir), '{}/../{}'.format(baseDir, patternName))
except FileExistsError:
    print(red('failed: this pattern already exists!'))
else:
    print(green('success!'))