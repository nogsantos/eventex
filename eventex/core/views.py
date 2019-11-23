from django.shortcuts import render, get_object_or_404

from eventex.core.models import Speaker, Talk


def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker/detail.html', {'speaker': speaker})


def talk_list(request):
    """
    When needs an API Mock, example:

    speaker = Speaker(
        name='Fabricio Nogueira',
        slug='fabricio-nogueira'
    )
    course = [
        dict(title='Course title',
             start='09:00',
             description='Course description',
             speakers={'all': [speaker]})
    ]
    """

    """
    Concatenate the list:

    at_morning = (
            list(Talk.objects.at_morning()) +
            list(Course.objects.at_morning())
    )
    at_morning.sort(key=lambda o: o.start)

    at_afternoon = (
            list(Talk.objects.at_afternoon()) +
            list(Course.objects.at_afternoon())
    )
    at_morning.sort(key=lambda o: o.start)
    """
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    }
    return render(request, 'core/talk/list.html', context)
