#!/usr/bin/env bash


# show routers
# ip netns
# delete routers
# sudo ip netns del 'variable'
sudo ip netns del howard-nrtr
sudo ip netns del michael-srtr
sudo ip netns del camilo-ertr
sudo ip netns del ming-wrtr
sudo ip netns del lnd-nat-cor

# show hosts
# ip netns
# delete hosts
# sudo ip netns del 'variable'
sudo ip netns del chrys-nhost
sudo ip netns del david-shost
sudo ip netns del abdul-ehost
sudo ip netns del mark-whost


# show bridges
# ip link show type bridge
# delete bridges
# sudo ip link del dev 'variable'
sudo ip link del dev North-bridge
sudo ip link del dev South-bridge
sudo ip link del dev East-bridge
sudo ip link del dev West-bridge


# show veths
# ip link show type veth
# delete veths
# sudo ip netns exec bowser ip link delete bowser2net
# deleting the bridges in the step above will automatically delete veths


