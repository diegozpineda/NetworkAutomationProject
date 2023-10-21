#!/bin/bash
sudo /usr/bin/qemu-system-x86_64 \
   -enable-kvm \
   -drive file=/var/kvm/images/vm-west.img,if=virtio \
   -cdrom vm-config/cloud-init-vm2.iso \
   -display curses \
   -nographic \
   -smp cpus=1 \
   -m 1G \
   -net nic,netdev=tap2,macaddr=aa:a3:a3:75:c7:5e \
   -netdev bridge,id=tap2,br=West-bridge \
   -d int \
   -D /var/log/qemu/qemu2.log    
