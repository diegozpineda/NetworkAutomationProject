#!/bin/bash
#
# del proj stuff
#
echo -e "Remove all netns"
a=$(sudo ip netns list)
for i in $a; do sudo ip netns del $i; done
echo -e "\nValidate all netns have been removed\n\n"
sudo ip netns list

echo -e "Remove all bridge interfaces\n" 
a=$(brctl show | grep "\-bridge" | cut -f 1)
for i in $a; do sudo ip link del dev $i; done
echo -e "Validate all bridges have been removed\n\n"
brctl show

echo -e "Remove all remaining veth interfaces\n"
a=$(ip link show type veth | cut -d ' ' -f 2 | cut -f 1 -d '@' | egrep -v veth)
for i in $a; do sudo ip link del $i; done
echo -e "Validate all veth interfaces have been removed\n\n"
sudo ip link show type veth

# validate
#sudo ip netns list
#brctl show
# EOF
