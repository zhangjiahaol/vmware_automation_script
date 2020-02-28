# vmware automation script
author:jiahao
## execute command example

## deploy VM
execute command example:
```
ansible-playbook vcenter_create_from_template.yml -e '{"vcenter_hostname":"192.168.1.250","vcenter_username":"administrator@vsphere.local","vcenter_password":"SHqz8866.","vm_name":"centos7_192.168.1.67","datacenter":"Datacenter","esxi_hostname":"192.168.1.161","annotation":"ansible auto created, IP: 192.168.1.67","num_cpus":"8","num_cpu_cores_per_socket":"1","memory_mb":"8192","disk_size_gb":"100","disk_type":"thin","disk_datastore":"datastore_161","networks_name":"VM Network","networks_type":"static","ip":"192.168.1.67","netmask":"255.255.255.0","gateway":"192.168.1.1","hostname":"shqz-67","dns1":"192.168.1.1","dns2":"114.114.114.114","template":"centos7_template_0228"}'
```
## delete VM
execute command example:
```
ansible-playbook vcenter_delete.yml -e '{"vcenter_hostname":"192.168.1.250","vcenter_username":"administrator@vsphere.local","vcenter_password":"SHqz8866.","vm_name":"centos7_192.168.1.67","datacenter":"Datacenter","esxi_hostname":"192.168.1.161"}'
```
## power VM Management
The available parameters are: powered-off/powered-on/shutdown-guest
```
ansible-playbook vcenter_powerstate.yml -e '{"vcenter_hostname":"192.168.1.250","vcenter_username":"administrator@vsphere.local","vcenter_password":"SHqz8866.","vm_name":"centos7_192.168.1.67","state":"powered-off"}'
```
## snapshot VM Management
The available parameters are: present/absent/revert/remove_all
```
ansible-playbook vcenter_snapshot.yml -e '{"vcenter_hostname":"192.168.1.250","vcenter_username":"administrator@vsphere.local","vcenter_password":"SHqz8866.","vm_name":"centos7_192.168.1.67","datacenter":"Datacenter","state":"present","snapshot_name":"2020_0228_0912","description":"ansible automation create."}'
```

## getallvms.py
```
execute command example:
python getallvms.py --host='192.168.1.250' --user='administrator@vsphere.local' --password='SHqz8866.' --disable_ssl_verification
```
## vmware_connect_web_console.py
```
execute command example:
python3 vmware_connect_web_console.py --host='192.168.1.250' --username='administrator@vsphere.local' --password='SHqz8866.' --vm-name='CentOS7_7_192.168.1.206'
```
