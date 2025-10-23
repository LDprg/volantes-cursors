#!/usr/bin/python
import os
import shutil
import re
import json

dir_conf = "./src/config/"
file_list = "./src/cursorList"

def gen_xcursors(NAME, dir_src, dir_out):
    with open(file_list, "r") as f:
        lines = f.readlines()
        for line in lines:
            file = re.findall(r"(.*) (.*)", line)
            if len(file) > 0:
                file = file[0]
                with open(dir_out + file[0], "w") as c:
                    c.write(file[1])

    os.system("kcursorgen --svg-theme-to-xcursor --svg-dir=\"" + dir_src + "\" --xcursor-dir=\"" + dir_out + "\" --sizes=24 --scales=1,2.5,3")


def create_cursors(NAME):
    dir_src = "./src/" + NAME + "/"
    dir_base = "./build/" + NAME + "/"
    dir_out = dir_base + "cursors_scalable/"
    dir_png = dir_base + "cursors/"
    files = os.listdir(dir_src)

    if os.path.isdir(dir_base):
        shutil.rmtree(dir_base)
    
    if not os.path.isdir(dir_png):
        os.makedirs(dir_png)

    os.makedirs(dir_out)

    with open(dir_base + "index.theme", "w") as f:
        f.write(
            "[Icon Theme]\n" + 
            "Name=Volantes Cursors\n" +
            "Comment=design by varlesh\n"
            )

    for file in files:
        if file.endswith("_24.svg"):
            name = file.removesuffix("_24.svg")

            if file.startswith("wait"):
                path = "wait"
            elif file.startswith("progress"):
                path = "progress"
            else:
                path = name

            dir_cur = dir_out + path + "/"

            if not os.path.isdir(dir_cur):
                os.makedirs(dir_cur)

            shutil.copy(dir_src + name + ".svg", dir_cur)
            
            with open(dir_conf + path + ".cursor") as f:
                frames = f.read()
                frames = re.findall(r"24 *([0-9]+) *([0-9]+) *(.*)_24_24.png *([0-9]+)?", frames)
                
                data = []

                for frame in frames:
                    hotspot_x = int(frame[0])
                    hotspot_y = int(frame[1])
                    filename = str(frame[2])
                    animation = str(frame[3])
                    
                    item = {
                        "filename": filename + ".svg",
                        "hotspot_x": hotspot_x,
                        "hotspot_y": hotspot_y,
                        "nominal_size": 24,
                    }

                    if animation.isdecimal():
                        item["delay"] = int(animation)

                    data.append(item)

                with open(dir_cur + "metadata.json", 'w') as j:
                    json.dump(data, j, indent=4)

    gen_xcursors(NAME, dir_out, dir_png)

    os.system("cd build && tar -cf " + NAME.replace("_", "-") + ".tar.gz " + NAME)


dir_base = "./build"
if os.path.isdir(dir_base):
    shutil.rmtree(dir_base)

create_cursors("volantes_cursors")
create_cursors("volantes_light_cursors")

