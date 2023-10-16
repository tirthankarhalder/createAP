import os
commandsList=[
            "sudo apt install hostapd",
            "sudo systemctl unmask hostapd",
            "sudo systemctl enable hostapd",
            "sudo apt install dnsmasq",
            "sudo DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent",
            "sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE",
            "sudo netfilter-persistent save",
            "sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig",
            "sudo rfkill unblock wlan",
            "sudo systemctl reboot"]
flag =0
for command in commandsList:
    
    if flag==5:
        dhcpdfile = open("/etc/dhcpcd.conf","a")
        dhcpdContent = ["interface wlan1\n","   static ip_address=192.168.4.1/24\n","   nohook wpa_supplicant"]
        dhcpdfile.writelines(dhcpdContent)
        dhcpdfile.close()
        print(flag,"Edit dhcpd.conf")
        flag+=1
    if flag==6:
        routedfile = open("/etc/sysctl.d/routed-ap.conf","a")
        routedapContent = ["# Enable IPv4 routing\n","net.ipv4.ip_forward=1"]
        routedfile.writelines(routedapContent)
        routedfile.close()
        print(flag,"Edit routed-ap.conf")
        flag+=1
    if flag==10:
        dnsmasqfile = open("/etc/dnsmasq.conf","a")
        dnsmasqContent = ["# Listening interface\n","interface=wlan1 \n","# Pool of IP addresses served via DHCP\n",
        "dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h\n","# Local wireless DNS domain\n",
        "domain=wlan\n","# Alias for this router\n","address=/gw.wlan/192.168.4.1"]
        dnsmasqfile.writelines(dnsmasqContent)
        dnsmasqfile.close()
        print(flag,"Edit dnsmasq.conf")
        flag+=1
    if flag==12:
        hostapdfile = open("/etc/hostapd/hostapd.conf","a")
        hostapdContent = ["country_code=IN\n",
                        "interface=wlan1\n",
                        "ssid=RpiN\n",
                        "hw_mode=g\n",
                        "channel=13\n",
                        "macaddr_acl=0\n",
                        "ignore_broadcast_ssid=0\n",
                        "wpa=2\n",
                        "wpa_passphrase=password\n",
                        "wpa_key_mgmt=WPA-PSK\n",
                        "wpa_pairwise=TKIP\n",
                        "rsn_pairwise=CCMP"]
        hostapdfile.writelines(hostapdContent)
        hostapdfile.close()
        print(flag,"Edit hostapd.conf")
        flag+=1
    print(flag,command)
    os.system(command)
    #subprocess.run(command)
    flag+=1


