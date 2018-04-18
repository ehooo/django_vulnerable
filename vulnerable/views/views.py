from django.views.generic import TemplateView
from django.conf import settings
from django.utils.html import mark_safe, escape
import os
import codecs
import markdown


class AboutView(TemplateView):
    template_name = "vulnerable/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        readme_file = os.path.join(settings.BASE_DIR, 'README.md')
        open_file = kwargs.get('path', '').strip('/').lower()
        try:
            if not open_file:
                open_file = readme_file
            ext = open_file.rsplit('.')[-1]
            input_file = codecs.open(open_file, mode="r", encoding="utf-8")
            text = input_file.read()
            if ext in ['md']:
                text = mark_safe(markdown.markdown(text))
            elif ext in ['py', 'html', 'js', 'css']:
                lang = ext
                if ext in ['py', 'html']:
                    lang = 'django'
                text = '<h4>{file}</h4><pre><code class="{lang} hljs">{code}</code></pre>'.format(
                    file=open_file,
                    lang=lang,
                    code=escape(text)
                )
                text = mark_safe(text)
            context.update({
                'about': text
            })
        except Exception as ex:
            context.update({
                'about': "{}: {}".format(ex.__class__.__name__, ex)
            })
            pass
        return context


class VulnerabilitiesListView(TemplateView):
    template_name = "vulnerable/list.html"

    def get_context_data(self, **kwargs):
        context = super(VulnerabilitiesListView, self).get_context_data()

        return context

