from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Total

#
def all_blogs(request):
    # return HttpResponse("Here I am today ")
    totals = Total.objects.order_by('-date') #give me most current 2

    # totals = Total.objects.order_by('-date')[:2] #give me most current 2
    # totals = Total.objects.order_by('-date') #sorting
    # totals = Total.objects.all()
    # context = {'totals':totals}

    # return render(request, 'blog/all_blogs.html', context)
    return render(request, 'blog/all_blogs.html', {'totals' : totals})

def testpage(request, blog_id):
    print("TEST VIEW")
    total = get_object_or_404(Total, pk=blog_id)
    return render(request, 'blog/testpage.html', {'total': total})
    # return render(request, 'blog/testpage.html', {'id': blog_id})



def detail(request, blog_id):
    print('Detail here')
    # blog = get_object_or_404(Total, pk=blog_id)
    return render(request, 'blog/detail.html', {'id':blog_id})

    # return render(request, 'blog/detail1.html', {'blog' :blog})
