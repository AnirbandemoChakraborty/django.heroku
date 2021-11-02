from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name ='index.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in he publisher
        context['name'] = 'Anirban'
        context['country'] = 'India'
        list = [1,2,3]
        context['list']= list
        return context
class AboutView(TemplateView):
    template_name = 'about.html'

