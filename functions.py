import json
from pprint import pprint


def load_file(files, mode, code, id_l=0, new_file=0):
    """
    Открытие файла и выполнение заданных действий
    :param files:Имя файла
    :param mode: метод чтение файла
    :param code: кодировка файла
    :param id_l: метод обработки файла
    :param new_file: куда записывать изменение файла
    :return: вывод результата
    """
    with open(files, mode, encoding=code) as file:
        if id_l == 0:
            return json.load(file)
        if id_l == 1:
            return file.read()
        if id_l == 2 and new_file != 0:
            file.write(new_file)
            print(files)
        if id_l == 3 and new_file != 0:
            json.dump(new_file, file, ensure_ascii=False, indent=4)
            print(files)


def index_tag(list_data):
    found_tags = {}
    for i_x, content in enumerate(list_data):
        t = content["content"].split(" ")
        list_content = [i for i in t if i.startswith("#")]
        print(list_content)
        found_tags = {i_x,list(lambda x: True if (len(x) > 0) else False, list_content)}
    print(found_tags)
