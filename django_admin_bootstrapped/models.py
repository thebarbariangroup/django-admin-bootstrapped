import django
from django.conf import settings
from django import forms
from django.contrib.admin.templatetags.admin_static import static

#monkey patch in support for bootstrap
@property
def media(self):
    extra = '' if settings.DEBUG else '.min'
    js = [
        'core.js',
        'admin/RelatedObjectLookups.js',
        'jquery%s.js' % extra,
        'jquery.init.js',
        'bootstrap%s.js' % extra
    ]
    if self.actions is not None:
        js.append('actions%s.js' % extra)
    if self.prepopulated_fields:
        js.extend(['urlify.js', 'prepopulate%s.js' % extra])
    return forms.Media(js=[static('admin/js/%s' % url) for url in js])

django.contrib.admin.options.ModelAdmin.media = media

