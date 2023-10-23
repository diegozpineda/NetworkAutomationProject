# OTS Capabilities Acceleration Program (CAP)
## 'CAP'Stone Network Automation Project
#### Primary Contributions by Diego Pineda and Ryan McNair
[![License][License-img]][License-url] ![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/diegozpineda/NetworkAutomationProject) ![GitHub repo size](https://img.shields.io/github/repo-size/diegozpineda/NetworkAutomationProject)  ![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/diegozpineda/NetworkAutomationProject) ![GitHub issues](https://img.shields.io/github/issues/diegozpineda/NetworkAutomationProject) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/diegozpineda/NetworkAutomationProject) [![](https://tokei.rs/b1/github/diegozpineda/NetworkAutomationProject)](https://github.com/diegozpineda/NetworkAutomationProject)

[License-img]: https://img.shields.io/github/license/larymak/Python-project-Scripts
[License-url]: https://www.gnu.org/licenses/gpl-3.0.en.html


## 'CAP'Stone Network Automation Project

    This project was designed for and created as a practice to simulate a 
    real-world scenario for building a network using automation tools.

    The entire project has been done using Ansible Playbooks, and although
    we did end up hard-coding some data, most of the Playbooks are setup
    to be dynamic. If the data file is updated, the 95% of the coding does
    not need to be altered.

### 1) Objectives
    ![](/CAP-Stone Newtork Diagram.png)

### 2) Network Topology
    A visual diagram of the network topology can be found in the network_diagram.pdf file.
    
    The network consists of a core router that is connected to the Internet and four
    internal routers. Each of the internal routers is connected to a bridge, and each
    bridge has a host connected. By design this network has been built for expandability, but not
    for redundancy or for being highly available.

### 2) Ansible Playbook
#### - [Deploy Namespaces Play](net_playbook-namespace.yml)
#### - Deploy Bridge Interfaces Play
#### - Deploy Host Veths Play
#### - Deploy Router Veths Play
#### - Assign LAN Host IPs Play
#### - Assign WAN Host IPs Play
#### - Deploy Core Router Veths Play
#### - Assign Core Router IPs Play
#### - Assign WAN Core IPs Play
#### - Creat NAT Interfaces Play
#### - Enable IP Forwarding Play
#### - Enable IP Routes Play
#### - Enable IPTables Play
#### - Enable Network-Wide Ping Play

