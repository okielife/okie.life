import json
import os


dir_path = os.path.dirname(os.path.realpath(__file__))


def json_to_string(obj):
    return json.dumps(obj)


def json_to_object(filename):
    file_path = os.path.join(dir_path, 'data', filename)
    if not os.path.exists(file_path):
        return None
    return json.load(open(file_path))


def get_all():
    ret_dict = dict()
    ret_dict['degrees'] = get_education()
    ret_dict['pubs'] = get_publications()
    ret_dict['person'] = get_person()
    ret_dict['experiences'] = get_experience()
    ret_dict['skills'] = get_skills()
    ret_dict['memberships'] = get_memberships()
    ret_dict['projects'] = get_projects()
    return ret_dict


def get_person():
    full_object = json_to_object("person.json")
    return full_object


def get_education():
    full_object = json_to_object("education.json")
    return full_object["degrees"]


def get_publications():
    full_object = json_to_object("publications.json")
    return full_object["publications"]


def get_experience():
    full_object = json_to_object("experience.json")
    return full_object["experience"]


def get_skills():
    full_object = json_to_object("skills.json")
    return full_object["skills"]


def get_memberships():
    full_object = json_to_object("memberships.json")
    return full_object["memberships"]


def get_projects():
    full_object = json_to_object("projects.json")
    return full_object["projects"]
