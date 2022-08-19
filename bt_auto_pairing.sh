#!/bin/bash
bluetoothctl <<EOF
power on
discoverable on
agent NoInputNoOutput
default-agent
pairable on
EOF
