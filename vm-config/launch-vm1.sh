#!/bin/bash
sudo /usr/bin/qemu-system-x86_64 \
   -enable-kvm \
   -drive file=/var/kvm/images/vm-north.img,if=virtio \
   -cdrom /var/kvm/images/cloud-init-vm1.iso \
   -display curses \
   -nographic \
   -smp cpus=1 \
   -m 1G \
   -net nic,netdev=tap1,macaddr=aa:a3:a3:af:50:24 \
   -netdev bridge,id=tap1,br=North-bridge \
   -d int \
   -D /var/log/qemu/qemu.log    
