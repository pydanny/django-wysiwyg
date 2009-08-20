from django.shortcuts import render_to_response

def basic_test(request):
    return render_to_response("basic_test.html")
