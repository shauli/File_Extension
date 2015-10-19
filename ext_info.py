import sys, os
from pathlib import Path
from collections import defaultdict

def create_files():
    return {
        'counter': 0,
        'size': 0,
    }


files = defaultdict(create_files)

if len(sys.argv) <= 1:
	print ('usage: ext_info.py path')
	print ('displays number of files and total size of files per extension in the specified path.')
	sys.exit()

folder = Path(sys.argv[1])
for p in folder.iterdir():
	if (p.is_file()):
		fileName = os.path.splitext(str(p))[1][1:]
		if (fileName == ''):
			fileName = '.'
		files[fileName]['counter'] += 1
		files[fileName]['size'] += p.stat().st_size

for name, info in files.items():
    print(name, info['counter'], info['size'])