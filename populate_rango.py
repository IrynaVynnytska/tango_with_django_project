import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                    'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',
        'likes': 0,
        'views': 2344},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
            'likes': 0,
        'views': 5677},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/',
        'likes': 0,
        'views': 876} ]
    
    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'likes': 0,
        'views': 345},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/',
        'likes': 0,
        'views': 7665},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/',
        'likes': 0,
        'views': 3445} ]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
        'likes': 0,
        'views': 34},
        {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'likes': 0,
        'views': 1203} ]

    cats = {
        'Python': {'pages': python_pages, "views": 128, "likes": 64},
        'Django': {'pages': django_pages, "views": 64, "likes": 32},
        'Other Frameworks': {'pages': other_pages, "views": 32, "likes": 16} }
    
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'], p['likes'])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0, likes=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.likes=likes
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views = views, likes = likes)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
