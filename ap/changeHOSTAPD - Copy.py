import os
import time 
# print("################# Initializing Hostapd Configauration Changing Menu ################")
# commandsList=[
#             "sudo apt install hostapd"
#             "sudo systemctl unmask hostapd",
#             "sudo systemctl enable hostapd"]
# for command in commandsList:
#     print(command)
#     os.system(command)
            
hostpdConflist={1:"20 Mhz IEEE 802.11n ",
                2:"40 Mhz IEEE 802.11n ",
                3:"20 Mhz IEEE 802.11ac",
                4:"40 Mhz IEEE 802.11ac",
                5:"80 Mhz IEEE 802.11ac"}
key =1
for conf in hostpdConflist:
    print(hostpdConflist[conf],"               To Activate Press",key)
    key+=1
pressedKey =int(input())
if pressedKey==1:
    file = open("/etc/hostapd/hostapd.conf","w+")
    hostapdContent = ["country_code=IN\n",
                    "interface=wlan1\n"
                    "ssid=RpiN20n\n",
                    "hw_mode=g\n",
                    "ieee80211n=1\n",
                    "require_ht=1\n",
                    "ht_capab=[MAX-AMSDU-3839][HT40+][SHORT-GI-20][SHORT-GI-40][DSSS_CCK-40]\n",
                    "channel=3\n",
                    "wmm_enabled=1\n",
                    "macaddr_acl=0\n",
                    "logger_syslog=0\n",
                    "logger_syslog_level=4\n",
                    "logger_stdout=-1\n",
                    "logger_stdout_level=0\n",
                    "ignore_broadcast_ssid=0"]
    file.writelines(hostapdContent)
    file.close()
    print(hostpdConflist[pressedKey],"       is Activated")
    print("Rebooting System......")
    time.sleep(3)
    os.system("sudo systemctl reboot")
    # subprocess.run(command)
elif pressedKey==2:
    file = open("/etc/hostapd/hostapd.conf","w")
    hostapdContent = [
                    "country_code=IN\n",
                    "interface=wlan1\n",
                    "ssid=RpiN40n\n",
                    "hw_mode=a\n",
                    "ieee80211n=1\n",
                    "vht_oper_chwidth=1\n",
                    "ht_capab=[MAX-AMSDU-3839][HT40+][SHORT-GI-40][DSSS_CCK-40]\n",
                    "channel=44\n",
                    "wmm_enabled=1\n",
                    "macaddr_acl=0\n",
                    "logger_syslog=0\n",
                    "logger_syslog_level=4\n",
                    "logger_stdout=-1\n",
                    "logger_stdout_level=0\n",
                    "ignore_broadcast_ssid=0\n"]
    file.writelines(hostapdContent)
    file.close()
    print(hostpdConflist[pressedKey],"       is Activated")
    print("Rebooting System......")
    time.sleep(3)
    os.system("sudo systemctl reboot")
elif pressedKey==3:
    file = open("/etc/hostapd/hostapd.conf","w")
    hostapdContent = ["country_code=IN\n",
                    "interface=wlan1\n",
                    "ssid=RpiN20ac\n",
                    "hw_mode=a\n",
                    "#ieee80211n=1\n",
                    "#require_ht=1\n",
                    "#ht_capab=[MAX-AMSDU-3839][HT40+][SHORT-GI-20][SHORT-GI-40][DSSS_CCK-40]\n",
                    "channel=36\n",
                    "wmm_enabled=1\n",
                    "macaddr_acl=0\n",
                    "logger_syslog=0\n",
                    "logger_syslog_level=4\n",
                    "logger_stdout=-1\n",
                    "logger_stdout_level=0\n",
                    "ignore_broadcast_ssid=0"]
    file.writelines(hostapdContent)
    file.close()
    print(hostpdConflist[pressedKey],"       is Activated")
    print("Rebooting System......")
    time.sleep(3)
    os.system("sudo systemctl reboot")
    # subprocess.run(command)
elif pressedKey==4:
    file = open("/etc/hostapd/hostapd.conf","w")
    hostapdContent = ["country_code=IN\n",
                    "interface=wlan1\n",
                    "ssid=RpiN40ac\n",
                    "hw_mode=a\n",
                    "ieee80211n=1\n",
                    "vht_oper_chwidth=0\n",
                    "ht_capab=[MAX-AMSDU-3839][HT40+][SHORT-GI-40][DSSS_CCK-40]\n",
                    "channel=44\n",
                    "wmm_enabled=1\n",
                    "macaddr_acl=0\n",
                    "logger_syslog=0\n",
                    "logger_syslog_level=4\n",
                    "logger_stdout=-1\n",
                    "logger_stdout_level=0\n",
                    "ignore_broadcast_ssid=0"]
    file.writelines(hostapdContent)
    file.close()
    print(hostpdConflist[pressedKey],"       is Activated")
    print("Rebooting System......")
    time.sleep(3)
    os.system("sudo systemctl reboot")
elif pressedKey==5:
    file = open("/etc/hostapd/hostapd.conf","w")
    hostapdContent = ["country_code=IN\n",
                    "ssid=RpiN80ac\n",
                    "#wpa_passphrase=gssst331\n",
                    "interface=wlan1\n",
                    "#wpa=2\n",
                    "#wpa_key_mgmt=WPA-PSK\n",
                    "#rsn_pairwise=CCMP\n",
                    "macaddr_acl=0\n",
                    "logger_syslog=0\n",
                    "logger_syslog_level=4\n",
                    "logger_stdout=-1\n",
                    "logger_stdout_level=0\n",
                    "hw_mode=a\n",
                    "wmm_enabled=1\n",
                    "ieee80211n=1\n",
                    "require_ht=1\n",
                    "ht_capab=[MAX-AMSDU-3839][HT40+][SHORT-GI-20][SHORT-GI-40][DSSS_CCK-40]\n",
                    "ieee80211ac=1\n",
                    "require_vht=1\n",
                    "ieee80211d=0\n",
                    "ieee80211h=0\n",
                    "vht_capab=[MAX-AMSDU-3839][SHORT-GI-80]\n",
                    "vht_oper_chwidth=1\n",
                    "channel=36\n",
                    "vht_oper_centr_freq_seg0_idx=42\n"]
    file.writelines(hostapdContent)
    file.close()
    print(hostpdConflist[pressedKey],"       is Activated")
    print("Rebooting System......")
    time.sleep(3)
    os.system("sudo systemctl reboot")
    # subprocess.run(command)

# print(hostpdConflist[pressedKey],"       is Activated")

