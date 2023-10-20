# Amazon Capabilities Acceleration Program (CAP)
## 'CAP'Stone Network Automation Project
#### Primary Contributions by Diego Pineda and Ryan McNair
[![Licence](https://img.shields.io/github/license/larymak/Python-project-Scripts)](https://www.gnu.org/licenses/gpl-3.0.en.html)


##'CAP'Stone Network Automation Project

    This project was designed for and created as a practice to simulate a 
    real-world scenario for building a network using automation tools.

    The entire project has been done using Ansible Playbooks, and although
    we did end up hard-coding some data, most of the Playbooks are setup
    to be dynamic. If the data file is updated, the 95% of the coding does
    not need to be altered.

###1) Network Topology
    A visual diagram of the network topology can be found in the network_diagram.pdf file.
    
    The network consists of a core router that is connected to the Internet and four
    internal routers. Each of the internal routers is connected to a bridge, and each
    bridge has a host connected. By design this network has been built for expandability, but not
    for redundancy or for being highly available.

    