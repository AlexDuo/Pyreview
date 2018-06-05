# Author: Real   
# CreateTime 5/30/2018-2:09 PM   
# IDE: PyCharm

import xml.etree.ElementTree as ET
#
tree = ET.parse("test.xml")

root = tree.getroot()

# print(root.tag)


# for child in root:
#     print(child.tag,child.attrib)
#     for i in child:
#         print(i.tag,i.attrib)

for node in root.iter('rank'):

    print(node.tag,node.text)