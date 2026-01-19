from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {"Title":"Home", "total_topics":4})

def about(request):
    return render(request, 'about.html', {"Title":"About"})

def topics(request):
    topics = [
              {'title': 'Installing Django', 'difficulty': 'Easy', 'description': 'Learn how to install Django on your system.', 'learned': True},
              {'title': 'Setting Up Django', 'difficulty': 'Medium', 'description': 'Set up your Django project and environment.', 'learned': True},
              {'title': 'Creating Project', 'difficulty': 'Easy', 'description': 'Create a new Django project.', 'learned': True},
              {'title': 'Template Inheritance', 'difficulty': 'Medium', 'description': 'Understand and use template inheritance in Django.', 'learned': False},
              ]
    return render(request, 'topics.html', {"Title":"Topics", "topics":topics})
