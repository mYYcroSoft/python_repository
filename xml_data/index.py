from xml.dom import minidom

file_s =  minidom.parse('plants.xml')
plants = file_s.getElementsByTagName('PLANT')


for plant in plants:
    price_el = plant.getElementsByTagName('PRICE')[0]
    el_name = plant.getElementsByTagName('BOTANICAL')[0]
    price = (float(price_el.firstChild.data.strip("$")))
    name = el_name.firstChild.data
    if price < 3:
        print(f'{name}   > ${price}')

