from django.shortcuts import render

# Create your views here.


def home(request):
    slug = request.GET.get('menu')
    if not slug:
        return render(request, 'home.html', context={
                'slug_status': None
            })
    return render(request, 'home.html', context={
            'slug_status': slug
        })
