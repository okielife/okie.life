from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def humans(request):
    return render(request, 'humans.html', context={'humans': """
/* TEAM */
    Main: Edwin Lee
    Contact: leeed2001 [at] gmail.com
    Github: @myoldmopar
    From: Tulsa, Oklahoma, United States

/* SITE */
    Last update: 2017-03
    Language: English
    Doctype: HTML5
    IDE: PyCharm
    Components: jQuery, Bootstrap, Django
"""})
