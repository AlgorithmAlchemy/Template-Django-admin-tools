# config/admin_tools.py
from django.utils.translation import gettext_lazy as _
from admin_tools.dashboard import Dashboard, AppIndexDashboard, modules



class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(
            modules.LinkList(
                title=_('Привет! Это кастомный дашборд'),
                layout='stacked',
                children=[
                    {
                        'title': _('Ссылка на Django'),
                        'url': 'https://www.djangoproject.com/',
                        'external': True,
                    },
                ]
            )
        )

class CustomAppIndexDashboard(AppIndexDashboard):
    pass
