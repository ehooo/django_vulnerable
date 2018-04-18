from django.utils.html import mark_safe
from django.views.generic import TemplateView


class XSSView(TemplateView):
    template_name = "vulnerable/xss.html"

    def get_context_data(self, **kwargs):
        context = super(XSSView, self).get_context_data()
        context['exploit'] = "<script>alert('XSS');</script>"
        return context

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :type request: django.http.HttpRequest
        :return: django.http.HttpResponse
        """
        context = self.get_context_data(**kwargs)
        name = request.POST.get('name')

        context.update({
            'message': mark_safe('<h6>Hello!! <b><i>{}</i></b></h6>'.format(name)),
            'helper': name
        })
        return self.render_to_response(context)

    def render_to_response(self, context, **response_kwargs):
        response = super(XSSView, self).render_to_response(context, **response_kwargs)
        response.setdefault('X-XSS-Protection', 0)
        return response
