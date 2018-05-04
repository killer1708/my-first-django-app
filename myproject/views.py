from django.http import HttpResponse

def hello(request):
    text = """<h1>Welcome to my App !</h1>"""
    return HttpResponse(text)
