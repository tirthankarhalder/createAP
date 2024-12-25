'''
# -*- coding: utf-8 -*-

Created on Thu Jan 12 20:56:18 2023

@author: xd

'''
from pathlib import Path

import pathlib
import shlex
import subprocess
from datetime import datetime

cmds_file = pathlib.Path(__file__).with_name("cmdclient.txt")
file_name = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")+".txt"
Path(file_name).touch(exist_ok= True)
output_file = pathlib.Path(__file__).with_name(file_name)
print(f"Output will be written to: {output_file}")
with open(cmds_file, encoding="utf-8") as commands, open(output_file, "w", encoding="utf-8") as output:
    for command in commands:
        print(f"Executing {command}")
        command = shlex.split(command)
        output.write(f"{datetime.now()}\n# {shlex.join(command)}\n")
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            output.write(result.stdout)
            if result.stderr:
                output.write(f"Error: {result.stderr}\n")
        except subprocess.CalledProcessError as e:
            output.write(f"Command failed with exit code {e.returncode}\n")
            output.write(f"Error output: {e.stderr}\n")
        

'''
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
import os
import sys

cmds_file = pathlib.Path(__file__).with_name("cmdclient.txt")
file_name = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")+".txt"
Path(file_name).touch(exist_ok= True)
output_file = pathlib.Path(__file__).with_name(file_name)
with open(cmds_file, encoding="utf-8") as commands, open(output_file, "w", encoding="utf-8") as output:
    for command in commands:
        print(command)
        command = shlex.split(command.strip())
        output.write(f"{datetime.now()}\n# {shlex.join(command)}\n")
        output.flush()
        #subprocess.run(command, stdout=output, stderr=subprocess.STDOUT, encoding="utf-8")
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        for line in process.stdout:
                sys.stdout.write(line)
                output.write(line)
        for line in process.stderr:
                sys.stderr.write(line)
                output.write(line)
        process.wait()
        
        

ans = input("Do you want to keep the file? yes/no: ")
if ans == "no":
        os.system(f"rm {file_name}")
        print("File deleted sucessfully")

        
'''

