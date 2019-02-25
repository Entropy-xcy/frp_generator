# Frp Generator

A helpful little tool for generating the config file for frp.

## Parameters

* -a or --append : Append to existing file; By default, the file to append is "frpc.ini"
* -g or --gui : Using GUI mode
* -l or --local_ip : Set the local ip address
* -s or --server_ip : Set the server ip address and port
* -p or --port : Set port to expose
* -ap or --additional_port : Set expose for ports on LAN ip other than which -l specifies. Notice that for this option 
you have to specifies a port on server side explicitly. Check for Example.5.
* -o or --output ： Set the name of the output file; By default, the output file is "frpc.ini"
* -h or --help ： Show this help page
* -v or --verbose ： Verbose mode

## Examples
1. Expose port 22 and port 80 to public IP 8.8.8.8 from LAN ip 0.0.0.0. Notice that the port on the server running frp service is 32767 <br/>
```python3 frp_generator.py -l 0.0.0.0 -p 22 -p 80 -s 8.8.8.8:32767```
2. Append one more port 443 to the existing config file "frpc.ini" <br/>
```python3 frp_generator.py -a -p 443```
3. Append port range from 6000 to 6010 to the existing config file "config.ini" <br/>
```python3 frp_generator.py -a config.ini -p 6000-6010```
4. Expose port 22 from LAN ip 0.0.0.0 to port 222 of public IP 8.8.8.8. Notice that the port on the server running frp service is 32767 <br/>
```python3 frp_generator.py -l 0.0.0.0 -p 22->222 -s 8.8.8.8:32767```
5. Expose port 22 from LAN ip 192.168.1.1 to port 22 and expose LAN ip 192.168.1.2 to port 222 on server 8.8.8.8:32767 <br/>
```python3 frp_generator.py -p 192.168.1.1:22->22 -p 192.168.1.2:22->222```