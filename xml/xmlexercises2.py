# Author: Real   
# CreateTime 5/30/2018-2:19 PM   
# IDE: PyCharm

import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')

root = tree.getroot()

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank == 2:
        root.remove(country)

tree.write('output.xml')
