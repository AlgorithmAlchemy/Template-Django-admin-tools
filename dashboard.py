from admin_tools.dashboard import modules, Dashboard

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
