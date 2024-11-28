#!/bin/bash



CONFIG_FILE="/etc/sysctl.d/routed-ap.conf"

# Pattern to match and remove the block
START_PATTERN="# Enable IPv4 routing"
END_PATTERN="net.ipv4.ip_forward=1"

# Check if the configuration block exists
if grep -q "$START_PATTERN" "$CONFIG_FILE"; then
    echo "Removing specified configuration block from $CONFIG_FILE..."
    sudo sed -i "/$START_PATTERN/,/$END_PATTERN/d" "$CONFIG_FILE"
    echo "Configuration block removed successfully."
else
    echo "Configuration block not found in $CONFIG_FILE. No changes made."
fi
``

CONFIG_FILE="/etc/dhcpcd.conf"

# Pattern to match and remove the block
START_PATTERN="interface wlan1"
END_PATTERN="nohook wpa_supplicant"

# Check if the configuration block exists
if grep -q "$START_PATTERN" "$CONFIG_FILE"; then
    echo "Removing specified configuration block from $CONFIG_FILE..."
    sudo sed -i "/$START_PATTERN/,/$END_PATTERN/d" "$CONFIG_FILE"
    echo "Configuration block removed successfully."
else
    echo "Configuration block not found in $CONFIG_FILE. No changes made."
fi

CONFIG_FILE="/etc/dnsmasq.conf"

# Pattern to match and remove the block
START_PATTERN="interface=wlan1"
END_PATTERN="address=/gw.wlan/192.168.4.1"

# Check if the configuration block exists
if grep -q "$START_PATTERN" "$CONFIG_FILE"; then
    echo "Removing specified configuration block from $CONFIG_FILE..."
    sudo sed -i "/$START_PATTERN/,/$END_PATTERN/d" "$CONFIG_FILE"
    echo "Configuration block removed successfully."
else
    echo "Configuration block not found in $CONFIG_FILE. No changes made."
fi



CONFIG_FILE="/etc/hostapd/hostapd.conf"

# Pattern to match and remove the block
START_PATTERN="country_code=IN"
END_PATTERN="rsn_pairwise=CCMP"

# Check if the configuration block exists
if grep -q "$START_PATTERN" "$CONFIG_FILE"; then
    echo "Removing specified configuration block from $CONFIG_FILE..."
    sudo sed -i "/$START_PATTERN/,/$END_PATTERN/d" "$CONFIG_FILE"
    echo "Configuration block removed successfully."
else
    echo "Configuration block not found in $CONFIG_FILE. No changes made."
fi


sudo apt uninstall hostapd
sudo apt uninstall dnsmasq


