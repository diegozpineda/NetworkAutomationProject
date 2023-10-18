#!/bin/bash
#
# del proj stuff
#
a=$(sudo ip netns list)
for i in $a; do sudo ip netns del $i; done
brctl
a=$(brctl show | grep "bridge" | tail -4 | cut -f 1)
for i in $a; do sudo ip link del dev $i; done

# validate
sudo ip netns list
brctl show
# EOF
