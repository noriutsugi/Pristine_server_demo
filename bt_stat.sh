#!/bin/bash
bt_address='B8:27:EB:A5:C1:87'
bluetoothctl show $bt_address | grep -E 'Powered:|Discoverable:|Pairable:|Discovering:'
