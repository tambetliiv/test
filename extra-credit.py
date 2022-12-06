import re

def convert_to_bin(ip_address):
  bin_ip = ''
  for octet in ip_address.split('.'):
    bin_ip = bin_ip + "{:08b}".format(int(octet))
  return bin_ip

def convert_to_dec(bin_ip):
  net_id_dec = ''
  for i in range(0, 32, 8):
    net_id_dec = net_id_dec + str(int(bin_ip[i:i+8], 2)) + '.'
  return net_id_dec.strip('.')

def find_ip(ip_address, prefix, mode = 0):
  # Mode 1 find broadcast address
  if mode == 1:
    bin_net_id = convert_to_bin(ip_address)[:prefix].ljust(32, '1')
  # Mode 2 find first usable IP
  elif mode == 2:
    bin_net_id = convert_to_bin(ip_address)[:prefix].ljust(31, '0') + '1'
  # default return Network ID
  else:
    bin_net_id = convert_to_bin(ip_address)[:prefix].ljust(32, '0')
  return convert_to_dec(bin_net_id)
  

file = open("input.txt", "r")

for line in file:
  ip = line.strip()
  ip_address = re.split('/|:', ip)[0]
  pref_port = int(re.split('/|:', ip)[1])
  # Port
  if ':' in ip:
    print(find_ip(ip_address, 22), end=' ')
    if pref_port > 0 and pref_port < 1024:
      print('Well-known port')
    elif pref_port >= 1024 and pref_port < 49152:
      print('Registered port')
    elif pref_port >= 49152 and pref_port <= 65535:
      print('Registered port')
    else:
      print('Unknown port')

  # Subnet
  if '/' in ip:
    print(find_ip(ip_address, pref_port, 2), end=' ')
    print(find_ip(ip_address, pref_port, 1))
    
    

file.close()


