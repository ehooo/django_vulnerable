import subprocess
import os

from django.views.generic import TemplateView


class CommandsView(TemplateView):
    template_name = "vulnerable/ping.html"

    def get_context_data(self, **kwargs):
        context = super(CommandsView, self).get_context_data()
        context['exploit'] = "1.1.1.1; ls > system_ls.txt\n"
        context['exploit'] += "1.1.1.1 && ls > system_ls.txt\n"
        context['exploit'] += "1.1.1.1 & ls > system_ls.txt\n"
        context['exploit'] += "1.1.1.1 | ls > system_ls.txt"
        context['modes'] = ['output', 'call', 'check', 'system']
        return context

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :type request: django.http.HttpRequest
        :return: django.http.HttpResponse
        """
        context = self.get_context_data(**kwargs)
        ip = request.POST.get('ip')
        mode = request.POST.get('mode')

        cmd = "ping -c 1 {ip}".format(ip=ip)
        try:
            output = b'Connection works'
            code = 0
            if mode == 'output':
                output = subprocess.check_output(cmd, shell=True)
            elif mode == 'call':
                code = subprocess.call(cmd, shell=True)
            elif mode == 'check':
                code = subprocess.check_call(cmd, shell=True)
            elif mode == 'system':
                code = os.system(cmd)
            else:
                output = ''
                context.update({
                    'errors': 'Mode not supported',
                })

            if code == 0:
                context.update({
                    'output': output.decode('utf-8'),
                })
            else:
                context.update({
                    'errors': 'Wrong code {}'.format(code),
                })
        except Exception as ex:
            context.update({
                'errors': "Error detected {}".format(ex),
            })
        finally:
            context.update({
                'helper': cmd,
            })

        return self.render_to_response(context)
