from django.views.generic import TemplateView
from vulnerable.models import User
from cassandra.cqlengine import connection


class BasicView(TemplateView):
    template_name = "vulnerable/login.html"

    def get_context_data(self, **kwargs):
        context = super(BasicView, self).get_context_data()
        context['exploit'] = ""
        return context

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :type request: django.http.HttpRequest
        :return: django.http.HttpResponse
        """
        context = self.get_context_data(**kwargs)
        email = request.POST.get('email')
        password = request.POST.get('password')

        query = "email='{email}' AND password='{password}'".format(
            email=email,
            password=password,
        )

        user = User.objects.filter()
        connection.execute(
            query,
            connection=user._get_connection()
        )
        context.update({
            'helper': query,
        })
        if bool(user):
            try:
                context.update({
                    'login': 'TODO'
                })
            except Exception as ex:
                context.update({
                    'errors': "User or password invalid",
                    'helper': "{}\n{}: {}".format(query, ex.__class__.__name__, ex),
                })
        else:
            context.update({
                'errors': "User or password invalid",
            })

        return self.render_to_response(context)
