#!/usr/bin/env bash

# delete routers
# sudo ip netns del 'variable'
sudo ip netns del howard-nrtr
sudo ip netns del michael-srtr
sudo ip netns del camilo-ertr
sudo ip netns del ming-wrtr
sudo ip netns del lnd-nat-cor

# delete hosts
# sudo ip netns del 'variable'
sudo ip netns del chrys-nhost
sudo ip netns del david-shost
sudo ip netns del abdul-ehost
sudo ip netns del mark-whost

# delete bridges
# sudo ip link del dev 'variable'
sudo ip link del dev North-bridge
sudo ip link del dev South-bridge
sudo ip link del dev East-bridge
sudo ip link del dev West-bridge
