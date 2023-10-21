#!/usr/bin/env python3
#
'''
Python script to deploy VM's via qemu using subprocess module
'''

#from qemu.qmp import QEMUMonitorProtocol
import subprocess
import requests
import os 
import time

def create_directories():
    '''
    Will create following directories if they don't exist
    /etc/qemu
    /var/kvm/images
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
    else:
        print(f'/etc/qemu exists')
    # create /var/kvm if it doesn't exist
    if os.path.isdir('/var/kvm/images') is False:
        os.mkdir('/var/kvm/images')
        # uid and gid are 1001 for student
        uid = 1001
        gid = 1001
        os.chown('/var/kvm/images', uid, gid)
        print(f'Created /var/kvm and set uid & gid to student')
    else:
        print(f'/var/kvm/images exists')
    return None

def create_bridgeconf():
    '''
    Create /etc/qemu and populate bridge.conf file
    with correct bridge settings
    '''

    # populate /etc/qemu/bridge.conf with North-bridge and West-bridge
    with open('/etc/qemu/bridge.conf', 'w') as bconf:
        bconf.write(f'allow North-bridge\n')
        bconf.write(f'allow West-bridge\n')
    
    print(f'Succesfully wrote settings to /etc/qemu/bridge.conf')
    return None

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
            print(f'VM config files do NOT exist')
            return False
        else:
            print(f'Confirmed VM config files exist.')
            return True

def check_vms():
    '''
    Simple check to see if vhd image files exist for vms
    '''
    vms = [
        '/var/kvm/images/vm-north.img',
        '/var/kvm/images/vm-west.img' ]
    for vm in vms:
        if os.path.isfile(vm) is False:
            print(f'VMs do Not exist')
            return False
        else:
            print(f'VMs Exist in /var/kvm')
            return True

def obtain_image():
    imgurl = 'https://static.alta3.com/projects/kvm/bionic-server-cloudimg-amd64.img'    
    vm1 = '/var/kvm/images/vm-north.img'
    vm2 = '/var/kvm/images/vm-west.img'
    
    if check_vms() is False:
        print(f'Downloading VMs')
        # get file if server returns OK    
        response = requests.get(imgurl)
        if response.status_code == 200:
            with open(vm1, "wb") as image1:
                image1.write(response.content)
            with open(vm2, "wb") as image2:
                image2.write(response.content)

def vm_isup(hostname: str):
    ping = [
        'ping',
        '-c',
        '2',
        hostname ]

    if subprocess.call(ping) == 0:
        return True
    else:
        return False

def launch_vms():
    qemu_binary = '/usr/bin/qemu-system-x86_64'
    north_path = '/var/kvm/images/vm-north.img'
    north_script = 'vm-config/launch-vm1.sh'
    west_path = '/var/kvm/images/vm-west.img'
    west_script = 'vm-config/launch-vm2.sh'
    bash = '/usr/bin/bash'
    vm1 = [
        bash,
        north_script ]

    vm2 = [
        bash,
        north_script ]

    if check_vmconfig() is True:
        print(f'Confirmed VM config files exist')
        print(f'Attempting to launch vm-north and vm-west')
        print(f'Will wait 80 seconds to confirm VMs are live')
        # use subprocess Popen to launch in a process outside of current python script
        # currently unsure how to not have qemu show vm in terminal window
        subprocess.Popen(north_script, close_fds=True)
        subprocess.Popen(west_script, close_fds=True)

        # Wait 30 seconds for VM's to load
        time.sleep(80)
        if vm_isup('vm-north') and vm_isup('vm-west'):                
            print(f'\n\nLaunched vm-north and vm-west succesfully') 
        else:
            print(f'\n Failed to launch VMs')

def main():
    create_directories()
    create_bridgeconf()
    obtain_image()
    launch_vms()

if __name__ == "__main__":
    main()