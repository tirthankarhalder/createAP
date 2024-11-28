#!/bin/bash
sudo apt update
sudo apt upgrade
sudo apt install raspberrypi-kernel-headers
CONFIG_FILE="/boot/config.txt"

# Configuration to append
CONFIG_CONTENT="
kernel=kernel7l.img
"

if grep -q "kernel=kernel7l.img" "$CONFIG_FILE"; then
    echo "Configuration for kernel=kernel7l.img already exists in $CONFIG_FILE. No changes made."
else
    echo "Appending configuration to $CONFIG_FILE..."
    echo "$CONFIG_CONTENT" | sudo tee -a "$CONFIG_FILE" > /dev/null
    echo "Configuration added successfully."
fi


