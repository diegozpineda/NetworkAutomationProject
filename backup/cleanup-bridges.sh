#!/usr/bin/env bash


# show bridges
# ip link show type bridge
# delete bridges
# sudo ip link del dev 'variable'
sudo ip link del dev North-bridge
sudo ip link del dev South-bridge
sudo ip link del dev East-bridge
sudo ip link del dev West-bridge
