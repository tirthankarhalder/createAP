import os
commandsList=["#sudo apt update &&sudo apt upgrade",
                "#sudo apt install raspberrypi-kernel-headers",
                "#git clone https://github.com/aircrack-ng/rtl8812au.git",
                "cd rtl8812au",
                "make",
                "sudo make install"
            ]
flag =0
for command in commandsList:
    print(flag,command)
    os.system(command)
    #subprocess.run(command)
    flag+=1


