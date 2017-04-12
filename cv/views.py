from django.shortcuts import render

from . import workers


def index(request):
    person = workers.get_person()
    return render(request, 'cv/index.html', context={'person': person})


def education(request):
    degrees = workers.get_education()
    return render(request, 'cv/education.html', context={'degrees': degrees})


def experience(request):
    experiences = workers.get_experience()
    return render(request, 'cv/experience.html', context={'experiences': experiences})


def skills(request):
    these_skills = workers.get_skills()
    return render(request, 'cv/skills.html', context={'skills': these_skills})


def memberships(request):
    these_memberships = workers.get_memberships()
    return render(request, 'cv/memberships.html', context={'memberships': these_memberships})


def projects(request):
    these_projects = workers.get_projects()
    return render(request, 'cv/projects.html', context={'projects': these_projects})


def publications(request):
    pubs = workers.get_publications()
    return render(request, 'cv/publications.html', context={'pubs': pubs})


def html(request):
    context = workers.get_all()
    return render(request, 'cv/html.html', context=context)


def pdf(request):
    context = workers.get_all()
    context['sanitized'] = True
    return render(request, 'cv/pdf.html', context=context)
