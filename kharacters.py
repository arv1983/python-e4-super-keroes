from csv import DictReader, DictWriter
from os import close
import os.path


def find_all_characters(filename):
    list_characters = []
    try:
        with open(filename, "r") as f:
            for row in DictReader(f):
                list_characters.append({'id': int(row['id']), 'name': row['name'],  'intelligence': int(row['intelligence']), 'power': int(row['power']), 'strength': int(row['strength']), 'agility': int(row['agility']) })
                return list_characters
    except FileNotFoundError:
        return []

def find_character_by_id(filename, character_id):
    heros = find_all_characters(filename)

    # print(heros)
    return [hero for hero in heros if hero['id'] == character_id][0]

    # with open(filename, "r+") as f:
    #     open_file = f.readlines()
    #     f.close()
    #     try:
    #         return dict(zip(open_file[0].split(','), open_file[character_id].split(',')))
    #     except:
    #         return None
        
def create_character(filename, **kwargs):
    headers = ['id', 'name', 'intelligence', 'power', 'strength', 'agility']
    if not os.path.isfile(filename):
        with open(filename, "a+") as f:
            writer = DictWriter(f, fieldnames=headers)
            writer.writeheader()
            f.close()

    with open(filename, "r+") as f:
        open_file = f.readlines()
        last_id = open_file[-1].split(',')[0]
        if last_id == 'id':
            last_id = 1
        else:
            last_id = int(last_id) + 1
        kwargs = [{**kwargs, 'id': last_id}]
        writer = DictWriter(f, fieldnames=headers)
        writer.writerows(kwargs)
        f.close()
    return kwargs[0]
    
# print(find_all_characters('teste.json'))
# print(find_character_by_id('teste.json', 1))
# print(create_character('exclui.json', **new)))

new = {
    'name': 'Batman',
    'intelligence': 7,
    'power': 4,
    'strength': 6,
    'agility': 8
}

print(create_character('testando.csv', **new))
