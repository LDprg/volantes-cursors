#!/usr/bin/python

import os


def rm_exist(path):
    if os.path.isdir(path):
        os.system("rm -r " + path)


rm_exist("/usr/share/icons/volantes_cursors/")
rm_exist("/usr/share/icons/volantes_light_cursors/")

os.system("cp -r ./build/volantes_cursors/ /usr/share/icons/")
os.system("cp -r ./build/volantes_light_cursors/ /usr/share/icons/")
