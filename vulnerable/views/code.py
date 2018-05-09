from django.views.generic import TemplateView
import math


class CodeView(TemplateView):
    template_name = "vulnerable/code.html"

    def get_context_data(self, **kwargs):
        context = super(CodeView, self).get_context_data(**kwargs)
        context['exploit'] = "__import__('os').kill(__import__('os').getpid(), __import__('signal').SIGTERM)\n" \
                             "math.sqrt(pow(2,4))"
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
                cmd = "result = {code}".format(code=code)
                exec(cmd)
                context.update({
                    'output': locals()['result'],
                })
            else:
                context.update({
                    'error': 'Mode not supported',
                })
        except Exception as ex:
            context.update({
                'errors': "Error detected {}".format(ex),
            })
        finally:
            var_locals = dict(locals())
            del(var_locals['context'])
            context.update({
                'locals': var_locals,
            })
            context.update({
                'helper': cmd,
            })

        return self.render_to_response(context)
