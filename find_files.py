import os
import shutil
import errno


DOT_FILES_NAMES = ['.vimrc', '.vim', '.zshrc', '.oh-my-zsh']

paths = []


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        if name in dirs:
            return os.path.join(root, name)


def copyanything(src, dst):
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)


for name in DOT_FILES_NAMES:
    paths.append(find(name, os.getenv('HOME')))

for path in paths:
    if path is not None:
        print(path)
        copyanything(path, './dots/' + os.path.basename(path))


# Delete everething from './dots' directory
# try:
#     shutil.rmtree('./dots/')
# except OSError as e:
#     if e.errno != errno.ENOENT:
#         raise
# #
