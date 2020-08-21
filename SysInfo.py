
'''
	Table of content of this Tut:
		1. Sys info
		2. CPU info
		3. Mem Usage
		4. Disck usage
		5. Network info
'''

import psutil
import platform
import os
from datetime import datetime

def clean():
	clr = os.system('clear')
	return clr
clean()

'''
	Scale bytes to its proper format
'''
def get_size(bytes, suffix="B"):
	factor = 1024
	for unit in ["", "K", "M", "G", "T", "P"]:
		if bytes < factor:
			return f"{bytes:.2f}{unit}{suffix}"
		bytes /= factor

# System info
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

# Getting the date and time the coputer was booted;

# Boot time
print("="*40, "Boot Time", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Time:{bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}")

# Cpu Information: total no of core, usage, etc
print("="*40, "CPU Info", "="*40)
	# number of cores
print("Physical Cores:", psutil.cpu_count(logical=False))
print("Total Cores:", psutil.cpu_count(logical=True))
	# cpu frequencies
cpufreq = psutil.cpu_freq()
print(f"\nMax Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
	# cpu usage
print("\nCpu Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
	print(f"\t\tCore{i}: {percentage}%")
print(f"Total Cpu Usage: {psutil.cpu_percent()}%")


# Network information
print("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
'''if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")'''
#get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
