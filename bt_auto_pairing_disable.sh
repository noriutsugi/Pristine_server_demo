#!/bin/bash
sudo bluetoothctl <<EOF
power on
discoverable off
pairable off
agent NoInputNoOutput
default-agent
EOF
