#!/usr/bin/env bash


# Kill any active gunicorn process if running 
echo -e "Stopping any active gunicorn processes if running\n\n"
sudo killall -9 gunicorn


# Kill any active VMs if running
echo -e "Stopping any active VMs if running\n\n"
sudo killall -9 qemu-system-x86_64

# delete routers namespaces
# sudo ip netns del 'variable'
echo -e "Deleting all router namespaces\n\n"
sudo ip netns del howard-nrtr
sudo ip netns del michael-srtr
sudo ip netns del camilo-ertr
sudo ip netns del ming-wrtr
sudo ip netns del lnd-nat-cor

# delete hosts
# sudo ip netns del 'variable'
echo -e "Deleting all host namespaces\n\n"
sudo ip netns del chrys-nhost
sudo ip netns del david-shost
sudo ip netns del abdul-ehost
sudo ip netns del mark-whost

# delete bridges
# sudo ip link del dev 'variable'
echo -e "Deleting all bridge interfaces\n\n"
sudo ip link del dev North-bridge
sudo ip link del dev South-bridge
sudo ip link del dev East-bridge
sudo ip link del dev West-bridge

# Validation
echo -e "Validate everything has been cleaned up\n"
#
echo -e "\nValidate gunicorn is not running\n"
ps aux | grep gunicorn
#
echo -e "\nValidate qemu is not running\n"
ps aux | grep qemu-system-x86_64
#
echo -e "\nValidate all namespaces have been deleted\n"
sudo ip netns list
#
echo -e "\nValidate all bridge interfaces have been deleted\n"
sudo brctl show
#
echo -e "\nCleanup complete\n"
#EOF

