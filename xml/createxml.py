# Author: Real   
# CreateTime 5/30/2018-2:30 PM   
# IDE: PyCharm

import xml.etree.ElementTree as et

fish = et.Element('Fish')
fish_name = et.SubElement(fish,'fish_name',attrib={'category':'Bass'})
fish_name.text = 'Rock Bass'



newxml = et.ElementTree(fish)


newxml.write('fish.xml',encoding='utf-8',xml_declaration= True)



