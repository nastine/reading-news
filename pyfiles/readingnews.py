import json
import xml.etree.ElementTree as ET
# from pprint import pprint

def reading_json():
    with open('newsfiles/newsafr.json') as f:
        json_data = json.load(f)
        
    words_list = []
    for news in json_data["rss"]["channel"]["items"]:
        for word in news["description"].split():
            if len(word) > 6:
                words_list.append(word.lower())

    result_json = {}
    for each in set(words_list):
        result_json[each] = words_list.count(each)

    sorted_by_value_json = sorted(result_json.items(), key=lambda kv: kv[1], reverse=True)

    print('\nReading from .json\nТоп 10 самых часто встречающихся в новостях слов длиннее 6 символов:')
    for request in sorted_by_value_json[:10]:
        print(f'- "{request[0]}"" встречается {request[1]} раз')

def reading_xml():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsfiles/newsafr.xml", parser)
    root = tree.getroot()
    channel = root.find("channel")
    items = channel.findall("item")
    words = []
    for item in items:
        news_text = item.find("description").text.split()
        for the_word in news_text:
            if len(the_word) > 6:
                words.append(the_word.lower())

    result_xml = {}
    for each_word in set(words):
        result_xml[each_word] = words.count(each_word)

    sorted_by_value_xml = sorted(result_xml.items(), key=lambda kv: kv[1], reverse=True)

    print('\nReading from .xml\nТоп 10 самых часто встречающихся в новостях слов длиннее 6 символов:')
    for request in sorted_by_value_xml[:10]:
        print(f'- "{request[0]}"" встречается {request[1]} раз')



reading_json()
reading_xml()