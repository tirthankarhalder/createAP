
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:56:18 2023

@author: xd
"""
from pathlib import Path
import pathlib
import shlex
import subprocess
from datetime import datetime

cmds_file = pathlib.Path(__file__).with_name("cmds.txt")
file_name = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")+".txt"
Path(file_name).touch(exist_ok= True)
output_file = pathlib.Path(__file__).with_name(file_name)
with open(cmds_file, encoding="utf-8") as commands, open(output_file, "w", encoding="utf-8") as output:
    for command in commands:
        command = shlex.split(command)
        output.write(f"{datetime.now()}\n# {shlex.join(command)}\n")
        output.flush()
        subprocess.run(command, stdout=output, stderr=subprocess.STDOUT, encoding="utf-8", shell=True)