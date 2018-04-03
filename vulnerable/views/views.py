from django.views.generic import TemplateView
from django.conf import settings
from django.utils.html import mark_safe
import os
import codecs
import markdown


class AboutView(TemplateView):
    template_name = "vulnerable/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        readme_file = os.path.join(settings.BASE_DIR, 'README.md')
        input_file = codecs.open(readme_file, mode="r", encoding="utf-8")
        text = input_file.read()
        html = markdown.markdown(text)
        context.update({
            'about': mark_safe(html)
        })
        return context


class VulnerabilitiesListView(TemplateView):
    template_name = "vulnerable/list.html"

    def get_context_data(self, **kwargs):
        context = super(VulnerabilitiesListView, self).get_context_data()

        return context

