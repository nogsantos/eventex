from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from eventex.core.models import Speaker, Talk

# class GenericHomeView(MultipleObjectMixin, TemplateView):
""" Method already implemented by TemplateView

def get(self, *args, **kwargs):
    context = self.get_context_data()
    return self.render_to_response(context)
"""

""" Method already implemented by TemplateResponseMixin

def render_to_response(self, context):
    return render(self.request, self.template_name, context)
"""

""" Method and attributes already implemented by MultipleObjectMixin

object_list = None
context_object_name = None

def get_context_data(self, **kwargs):
    context = {self.context_object_name: self.object_list}
    context.update(kwargs)
    return context
"""


class HomeView(ListView):
    template_name = 'index.html'
    model = Speaker


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
