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
        if not list_content:
            continue
        found_tags.update({i_x: []})
        for tag_list in list_content:
            temp_w = tag_list[1:]
            if tag_list.endswith("!"):
                temp_len = len(temp_w)
                found_tags[i_x].append(temp_w[:temp_len - 1])
            else:
                found_tags[i_x].append(temp_w)
    return found_tags


def list_tag(list_data):
    found_list_tags = set()
    print(list_data)
    for tag in list_data:
        for t in list_data[tag]:
            found_list_tags.add(t)
    return found_list_tags


def add_post(all_posts, post, file_post, mode, code):
    all_posts.append(post)
    with open(file_post, mode, encoding=code) as file:
        json.dump(all_posts, file, ensure_ascii=False, indent=4)




