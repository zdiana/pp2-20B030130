import json

# Load the JSON file
with open('sample-data.json', 'r') as f:
    data = json.load(f)

# Define the header for the output
header = 'DN'.ljust(50) + 'Description'.ljust(25) + 'Speed'.ljust(8) + 'MTU\n'
divider = '-' * 80 + '\n'

# Generate the output string
output = header + divider
for item in data:
    dn = item['fabric_intf_dn'].ljust(50)
    description = item['descr'].ljust(25)
    speed = item['eth_speed'].ljust(8) if 'eth_speed' in item else 'inherit'.ljust(8)
    mtu = str(item['mtu']).rjust(6) if 'mtu' in item else ''
    output += f"{dn} {description} {speed} {mtu}\n"

output += divider

# Print the output
print(output)
