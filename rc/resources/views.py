from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.utils.decorators import classonlymethod
from django.conf import settings
from aashe.aasheauth.middleware import SESSION_USER_DICT_KEY

MEMBER_ROLES = getattr(settings, 'AASHEAUTH_MEMBER_ROLES', ('Member', 'Guest', 'Staff'))

class ResourceItemListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(ResourceItemListView, self).get_context_data(
            **kwargs)
        opts = self.model._meta

        if not 'title' in context.keys():
            context['title'] = opts.verbose_name_plural.title()

        admin_change_url_name = 'admin:%s_%s_changelist' % (opts.app_label,
                                                            opts.object_name.lower())
        context['admin_changelist_url'] = reverse(admin_change_url_name)

        # So we can pass values from urls.py to templates:
        if self.kwargs:
            context.update(self.kwargs)

        return context
    
    def get_template_names(self):
        member = False
        
        if self.request.session.has_key(SESSION_USER_DICT_KEY):
            user_dict = self.request.session.get(SESSION_USER_DICT_KEY)
            for role in MEMBER_ROLES:
                if role in user_dict['roles'].values():
                    member = True
        
        try: 
          if not member and self.kwargs['member_only']:
              base_template = 'aashe/base_membersonly.html'
              model_template = "%s_membersonly.html" % self.context_object_name
              return[base_template, model_template];
          else:
              return super(ResourceItemListView, self).get_template_names()
        except:
          return super(ResourceItemListView, self).get_template_names()
