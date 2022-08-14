# - `load_candidates_from_json(path)` – возвращает список всех кандидатов
# - `get_candidate(candidate_id)` – возвращает одного кандидата по его id
# - `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
# - `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку

import json
from candidate import Candidate


def load_candidates_from_json() -> list[Candidate]:
    '''возвращает список всех кандидатов'''
    with open('candidates.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data



def get_candidate(candidate_id: int )-> Candidate:
    '''возвращает одного кандидата по его id'''
    for item in load_candidates_from_json():
        if item['id'] == candidate_id:
            return item


def get_candidates_by_name(candidate_name: str)->  list[Candidate]:
    '''возвращает кандидатов по имени'''
    name_list=[]
    for item in load_candidates_from_json():
        if item['name'] == candidate_name:
            name_list.append(item)
    return name_list

def get_candidates_by_skill(skill_name: str)->  list[Candidate]:
    '''возвращает кандидатов по навыку'''
    skill_list = []
    for item in load_candidates_from_json():
        if skill_name in item['skills'].lower().split(', '):
            skill_list.append(item)
    return skill_list

