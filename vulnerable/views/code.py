from django.views.generic import TemplateView


class CodeView(TemplateView):
    template_name = "vulnerable/code.html"

    def get_context_data(self, **kwargs):
        context = super(CodeView, self).get_context_data()
        context['exploit'] = "__import__('os').kill(__import__('os').getpid(), __import__('signal').SIGTERM)"
        context['modes'] = ['eval', 'exec']
        return context

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :type request: django.http.HttpRequest
        :return: django.http.HttpResponse
        """
        context = self.get_context_data(**kwargs)
        code = request.POST.get('code')
        mode = request.POST.get('mode')

        cmd = "{code}".format(code=code)
        try:
            output = ''
            if mode == 'eval':
                output = eval(cmd)
                context.update({
                    'output': output,
                })
            elif mode == 'exec':
                exec(cmd, globals(), locals())
                context.update({
                    'output': 'exec always returns None',
                })
            else:
                context.update({
                    'error': 'Mode not supported',
                })
        except Exception as ex:
            context.update({
                'error': "Error detected {}".format(ex),
            })
        finally:
            context.update({
                'globals': str(globals()),
                'locals': str(locals()),
            })
            context.update({
                'helper': cmd,
            })

        return self.render_to_response(context)
