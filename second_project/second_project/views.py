from django.http import HttpResponse


def home(request):
    return HttpResponse(
        
        
        '''This is home page
            <a href="/first_app/contact/"> Contact </a>
            <a href="/first_app/about/"> About </a>
                        <a href="/second_app/courses/"> Courses </a>
                        <a href="/second_app/feedback/"> Feedback</a>
        
        '''
    )