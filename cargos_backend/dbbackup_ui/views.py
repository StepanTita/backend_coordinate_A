from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from bridge.status_logger.status_logger import class_status_logger
from .forms import DatabaseBackupForm, MediaBackupForm


class BackupView(LoginRequiredMixin, UserPassesTestMixin, TemplateResponseMixin, View):
    template_name = 'dbbackup_ui/backup_view.html'

    def test_func(self):
        return self.request.user.is_superuser

    @class_status_logger
    def get(self, request, *args, **kwargs):
        # context = {
        #     'database_backup_form': DatabaseBackupForm(),
        #     'media_backup_form': MediaBackupForm(),
        #     'title': 'Backup Database and Media'
        # }

        context = {
            'database_backup_form': DatabaseBackupForm(),
            'media_backup_form': MediaBackupForm(),
            'title': 'Backup Database and Media'
        }
        context.update(admin.site.each_context(request))
        return self.render_to_response(self.update_context(context))

    @class_status_logger
    def post(self, request, *args, **kwargs):
        database_backup_form = DatabaseBackupForm(request.POST)
        media_backup_form = MediaBackupForm(request.POST)

        context = {
            'database_backup_form': database_backup_form,
            'media_backup_form': media_backup_form,
        }
        context.update(admin.site.each_context(request))

        outputfile, filename = None, None
        if 'savebackup' in request.POST and database_backup_form.is_valid():
            outputfile, filename = database_backup_form.do_backup()
        elif 'mediabackup' in request.POST and media_backup_form.is_valid():
            outputfile, filename = media_backup_form.do_backup()

        if outputfile and filename:
            response = HttpResponse(
                outputfile.read(),
                content_type="application/x-gzip"
            )
            response['Content-Disposition'] = 'inline; filename=' + filename
            return response

        return self.render_to_response(self.update_context(context))

    @class_status_logger
    def update_context(self, context):
        context.update({
            'title': 'Backup Database and Media'
        })
        context.update(admin.site.each_context(self.request))
        return context
