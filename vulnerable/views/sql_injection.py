from django.views.generic import TemplateView
from django.contrib.auth.models import User


class BasicView(TemplateView):
    template_name = "vulnerable/login.html"

    def get_context_data(self, **kwargs):
        context = super(BasicView, self).get_context_data()
        context['exploit'] = "' OR 1=1 --"
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

        sql = "SELECT * FROM auth_user WHERE email='{email}' AND password='{password}'".format(
            email=email,
            password=password,
        )

        user = User.objects.raw(sql)
        context.update({
            'helper': user.query,
        })
        if bool(user):
            try:
                context.update({
                    'login': user[0]
                })
            except Exception as ex:
                context.update({
                    'errors': "User or password invalid",
                    'helper': "{}\n{}: {}".format(user.query, ex.__class__.__name__, ex),
                })
        else:
            context.update({
                'errors': "User or password invalid",
            })

        return self.render_to_response(context)


class ExtraWhereView(TemplateView):
    template_name = "vulnerable/login.html"

    def get_context_data(self, **kwargs):
        context = super(ExtraWhereView, self).get_context_data()
        context['exploit'] = "') OR (''='"
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

        where = [
            "email='{email}'".format(email=email),
            "password='{password}'".format(password=password),
        ]
        user = User.objects.extra(where=where)
        context.update({
            'helper': user.query,
        })
        try:
            context.update({
                'login': user.get()
            })
        except Exception as ex:
            context.update({
                'errors': "User or password invalid",
                'helper': "{}\n{}: {}".format(user.query, ex.__class__.__name__, ex),
            })

        return self.render_to_response(context)

