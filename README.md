# Kushari IPMI

## Requirements
- Python2
- Packages in requirements.txt

## Installation
- Create virtual environment
`virtualenv -p /usr/bin/python2 venv`
- Load the env
`source venv/bin/activate`
- Install the requirements
`venv/bin/pip install -r requirements.txt`
- Run server locally or configure uwsgi
`venv/bin/python2 manage.py runserver 0.0.0.0:8000`

## Endpoints
### Chassis
##### Power on
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password
```
curl -s HOST:PORT/api/chassis/poweron/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD"
```

##### Power off
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password
```
curl -s HOST:PORT/api/chassis/poweroff/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD"
```

##### Power reset
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password
```
curl -s HOST:PORT/api/chassis/powerreset/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD"
```

##### Power cycle
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password
```
curl -s HOST:PORT/api/chassis/powercycle/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD"
```

##### UID control
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password, uid_status(Boolean)
```
curl -s HOST:PORT/api/chassis/uidcontrol/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD" \
 -d "uid_status=True"
```

##### Operating System shutdown
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password
```
curl -s HOST:PORT/api/chassis/osoff/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD"
```

##### Power Status
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password
```
curl -s HOST:PORT/api/chassis/powerstatus/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD"
```

### Network
##### BMC Info
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password
```
curl -s HOST:PORT/api/network/bmcinfo/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD"
```

##### BMC Info - Mac Address
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password
```
curl -s HOST:PORT/api/network/bmcinfo/macaddress/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD"
```

##### Ethernet Info - Mac Address
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password
```
curl -s HOST:PORT/api/eth0info/macaddress/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD"
```

### Boot
##### Configure Next boot
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password, boot_option, persist
```
curl -s HOST:PORT/api/boot/setnextboot/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD" \
 -d "boot_option=hd, network, optical, setup, default" \
 -d "persist=True, False"
 -d "uefiboot=True, False"
```

##### Configure Next boot and immediate reboot
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password, boot_option
```
curl -s HOST:PORT/api/boot/immediate/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD" \
 -d "boot_option=hd, network, optical, setup, default"
```

### Users
##### Control
- Request Type: POST
- Parameters: bmc_ip, bmc_username, bmc_password, uid, mode, password
```
curl -s HOST:PORT/api/users/control/ \
 -d "bmc_ip=BMC_IP" \
 -d "bmc_username=BMC_USERNAME" \
 -d "bmc_password=BMC_PASSWORD" \
 -d "uid=USER-ID-TO-MANAGE" \
 -d "mode=enable, disable, set_password" \
 -d "password=REQUIRED-PASSWORD"
```

## Inventory
### Chassis
##### Power on
- Request Type: POST
- Parameters: server_name
```
curl -s HOST:PORT/api/inventory/chassis/poweron/ \
 -d "server_name=CLIENT-SERVER-NAME"
```

##### Power off
- Request Type: POST
- Parameters: server_name
```
curl -s HOST:PORT/api/inventory/chassis/poweroff/ \
 -d "server_name=CLIENT-SERVER-NAME"
```

##### Power reset
- Request Type: POST
- Parameters: server_name
```
curl -s HOST:PORT/api/inventory/chassis/powerreset/ \
 -d "server_name=CLIENT-SERVER-NAME"
```

##### Operating System shutdown
- Request Type: POST
- Parameters: server_name
```
curl -s HOST:PORT/api/inventory/chassis/osoff/ \
 -d "server_name=CLIENT-SERVER-NAME"
```

##### Power Status
- Request Type: POST
- Parameters: server_name
```
curl -s HOST:PORT/api/inventory/chassis/powerstatus/ \
 -d "server_name=CLIENT-SERVER-NAME"
```

### Network
##### BMC Info
- Request Type: POST
- Parameters: server_name
```
curl -s HOST:PORT/api/inventory/network/bmcinfo/ \
 -d "server_name=CLIENT-SERVER-NAME"
```

##### BMC Info - Mac Address
- Request Type: POST
- Parameters: server_name
```
curl -s HOST:PORT/api/inventory/network/bmcinfo/macaddress/ \
 -d "server_name=CLIENT-SERVER-NAME"
```

##### Ethernet Info - Mac Address
- Request Type: POST
- Parameters: server_name
```
curl -s HOST:PORT/api/inventory/network/eth0info/macaddress/ \
 -d "server_name=CLIENT-SERVER-NAME"
```

### Boot
##### Configure Next boot
- Request Type: POST
- Parameters: server_name, boot_option, persist
```
curl -s HOST:PORT/api/inventory/boot/setnextboot/ \
 -d "server_name=CLIENT-SERVER-NAME" \
 -d "boot_option=hd, network, optical, setup, default" \
 -d "persist=True, False"
 -d "uefiboot=True, False"
```

##### Configure Next boot and immediate reboot
- Request Type: POST
- Parameters: server_name, boot_option
```
curl -s HOST:PORT/api/inventory/boot/immediate/ \
 -d "server_name=CLIENT-SERVER-NAME" \
 -d "boot_option=hd, network, optical, setup, default"
```

### Users
##### Control
- Request Type: POST
- Parameters: server_name, uid, mode, password
```
curl -s HOST:PORT/api/inventory/users/control/ \
 -d "server_name=CLIENT-SERVER-NAME" \
 -d "uid=USER-ID-TO-MANAGE" \
 -d "mode=enable, disable, set_password" \
 -d "password=REQUIRED-PASSWORD"
```