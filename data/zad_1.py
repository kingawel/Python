import xml.etree.ElementTree as element
tree = element.parse('capital.xml')
root = tree.getroot()
new_tag = "NEW"
for stolica in root.iter('stolica'):
	stolica.text = new_tag
tree.write('new_capital.xml')