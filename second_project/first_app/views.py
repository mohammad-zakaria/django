from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def contact(request):
    return HttpResponse('''
                        <h1> This contact page </h2>
                        <a href="/first_app/about/"> About </a>
                        <a href="/second_app/courses/"> Courses </a>
                        <a href="/second_app/feedback/"> Feedback</a>
                        
                        ''')

def about(request):
    return HttpResponse('''
                        
                        <h1> This is About Page</h1>
                        <a href="/first_app/contact/"> Contact</a>
                        <a href="/second_app/courses/"> Courses </a>
                        <a href="/second_app/feedback/"> Feedback</a>
                        
                        ''')