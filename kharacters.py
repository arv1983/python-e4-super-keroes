from csv import DictReader, DictWriter
from os import close
import os.path


def find_all_characters(filename):
    list = []
    with open(filename, "r") as f:
        for row in DictReader(f):
            list.append({'id': int(row['id']), 'name': row['name'],  'intelligence': int(row['intelligence']), 'power': int(row['power']), 'strength': int(row['strength']), 'agility': int(row['agility']) })
        if not list:
            return []
        else:
            return list


def find_character_by_id(filename, character_id):
    with open(filename, "r+") as f:
        open_file = f.readlines()
        f.close()
        try:
            return dict(zip(open_file[0].split(','), open_file[character_id].split(',')))
        except:
            return None
        
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
    return kwargs
    

print(find_all_characters('testando.csv'))