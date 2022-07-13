import requests
import xml.etree.ElementTree as ET


def dollar_rate():
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(response.content)
    dollar = tree.find('.//Valute[@ID="R01235"]').find('Value').text
    dollar = dollar.replace(',', '.')
    return float(dollar)


dollar_rate()
