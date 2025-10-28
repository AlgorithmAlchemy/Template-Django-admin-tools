# config/admin_tools.py
from django.utils.translation import gettext_lazy as _
from admin_tools.dashboard import Dashboard, AppIndexDashboard, modules


class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(modules.LinkList(
            title='Полезные ссылки',
            layout='inline',
            children=[
                {'title': 'Открыть сайт', 'url': '/', 'external': False},
                {'title': 'Документация Django', 'url': 'https://docs.djangoproject.com/'},
            ]
        ))


class CustomAppIndexDashboard(AppIndexDashboard):
    pass
