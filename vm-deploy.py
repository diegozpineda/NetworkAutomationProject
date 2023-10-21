#!/usr/bin/env python3
#
'''
Python script to deploy VM's via qemu using subprocess module
'''

#from qemu.qmp import QEMUMonitorProtocol
import subprocess
import requests
import os 

def create_directories():
    '''
    Will create following directories if they don't exist
    /etc/qemu
    /var/kvm
    will modify /var/kvm permissions
    '''
    # check if /etc/qemu exists
    # if not create it
    if os.path.isdir('/etc/qemu') is False:
        # make_directory = [
        #     'mkdir'
        #     '-p'
        #     '/etc/qemu']
        # subprocess.call(make_directory)
        os.mkdir('/etc/qemu')
        print(f'Created /etc/qemu')
    # create /var/kvm if it doesn't exist
    if os.path.isdir('/var/kvm') is False:
        os.mkdir('/var/kvm')
        # uid and gid are 1001 for student
        uid = 1001
        gid = 1001
        os.chown('/var/kvm', uid, gid)
        print(f'Created /var/kvm and set uid & gid to student')
    return None

def create_bridgeconf():
    '''
    Create /etc/qemu and populate bridge.conf file
    with correct bridge settings
    '''

    # populate /etc/qemu/bridge.conf with North-bridge and West-bridge
    with open('/etc/qemu/bridge.conf', 'w') as bconf:
        bconf.write(f'allow North-bridge')
        bconf.write(f'allow West-bridge')
    
    return None

def obtain_image():
    imgurl = 'https://static.alta3.com/projects/kvm/bionic-server-cloudimg-amd64.img'    
    vm1 = '/var/kvm/vm-north.iso'
    vm2 = '/var/kvm/vm-west.iso'

    # get file if server returns OK    
    response = requests.get(imgurl)
    if response.status_code == 200:
        with open(vm1, "wb") as image1:
            image1.write(response.content)
        with open(vm2, "wb") as image2:
            image2.write(response.content)

def check_vmconfig():
    '''
    Will check if vm_config directory exists and if required files exist
    '''
    files = [
        'cloud-init-vm1.iso',
        'cloud-init-vm2.iso',
        'launch-vm1.sh',
        'launch-vm2.sh']
    for file in files:
        path = './vm-config'
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath) is False:
            return False
    return True

def launch_vms():
    qemu_binary = '/usr/bin/qemu-system-x86_64'
    north_path = '/var/kvm/vm-north.iso'
    north_script = './vm-config/launch-vm1.sh'
    west_path = '/var/kvm/vm-west.iso'
    west_script = './vm-config/launch-vm2.sh'
    #vm1 = [
    #]
    subprocess.run(north_script)
    subprocess.run(west_script)

    return f'Launched vm-north and vm-west succesfully' 

def main():
    create_directories()
    create_bridgeconf()
    check_vmconfig()
    obtain_image()
    launch_vms()

if __name__ == "__main__":
    main()