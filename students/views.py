
from django.shortcuts import render

from post.models import News
from students.models import Students

def students_rating(request):

    context = {

        'row_posts': News.objects.all().order_by('-publication_date_time')[:5],
        'students': Students.objects.all()
    }

    return render(request, 'students_rating.html', context)

