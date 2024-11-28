# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:56:18 2023

@author: xd
"""

import pathlib
import shlex
import subprocess
from datetime import datetime
cmds_file = pathlib.Path(__file__).with_name("cmds.txt")
output_file = pathlib.Path(__file__).with_name("output.txt")
print(output_file)
with open(cmds_file, encoding="utf-8") as commands, open(output_file, "w", encoding="utf-8") as output:
    for command in commands:
        command = shlex.split(command)
        output.write(f"{datetime.now()}\n# {shlex.join(command)}\n")
        output.flush()
        subprocess.run(command, stdout=output, stderr=subprocess.STDOUT, encoding="utf-8",shell=True)