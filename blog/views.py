from django.shortcuts import render
# from .models import Another
#
# def all_blogs(request):
    # blogstuff = Another.objects.all()
    # return render(request, 'blog/all_blogs.html', {'blogstuff' : blogstuff})
#
#
#
def all_blogs(request):
    return render(request, 'blog/all_blogs.html')
