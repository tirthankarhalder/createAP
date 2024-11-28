#!/bin/bash

sudo apt install hostapd
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo apt install dnsmasq
sudo DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent

CONFIG_FILE="/etc/dhcpcd.conf"

# Configuration to append
CONFIG_CONTENT="
interface wlan1
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
"

if grep -q "interface wlan0" "$CONFIG_FILE"; then
    echo "Configuration for wlan0 already exists in $CONFIG_FILE. No changes made."
else
    echo "Appending configuration to $CONFIG_FILE..."
    echo "$CONFIG_CONTENT" | sudo tee -a "$CONFIG_FILE" > /dev/null
    echo "Configuration added successfully."
fi


CONFIG_FILE="/etc/sysctl.d/routed-ap.conf"

# Configuration to insert
CONFIG_CONTENT="
# Enable IPv4 routing
net.ipv4.ip_forward=1
"

if grep -q "net.ipv4.ip_forward=1" "$CONFIG_FILE"; then
    echo "IPv4 routing is already enabled in $CONFIG_FILE. No changes made."
else
    echo "Inserting IPv4 routing configuration into $CONFIG_FILE..."
    echo "$CONFIG_CONTENT" | sudo tee -a "$CONFIG_FILE" > /dev/null
    echo "Configuration added successfully."
fi

sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo netfilter-persistent save
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig

CONFIG_FILE="/etc/dnsmasq.conf"

# Configuration to insert
CONFIG_CONTENT="
interface=wlan1       # Listening interface
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
                      # Pool of IP addresses served via DHCP
domain=wlan           # Local wireless DNS domain
address=/gw.wlan/192.168.4.1
                      # Alias for this router
"

# Check if the configuration already exists
if grep -q "interface=wlan0" "$CONFIG_FILE"; then
    echo "Configuration for wlan0 already exists in $CONFIG_FILE. No changes made."
else
    echo "Appending configuration to $CONFIG_FILE..."
    echo "$CONFIG_CONTENT" | sudo tee -a "$CONFIG_FILE" > /dev/null
    echo "Configuration added successfully."
fi


sudo rfkill unblock wlan


CONFIG_FILE="/etc/hostapd/hostapd.conf"

# Configuration to insert
CONFIG_CONTENT="
country_code=IN
interface=wlan1
ssid=RpiNetwork
hw_mode=g
channel=13
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=AvadaKadavra
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
"

# Check if the configuration already exists
if grep -q "ssid=RpiNetwork" "$CONFIG_FILE"; then
    echo "SSID RpiNetwork already exists in $CONFIG_FILE. No changes made."
else
    echo "Appending configuration to $CONFIG_FILE..."
    echo "$CONFIG_CONTENT" | sudo tee "$CONFIG_FILE" > /dev/null
    echo "Configuration added successfully."
fi
echo "Finished Setup...................."
sudo systemctl reboot
