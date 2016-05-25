from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic import View

class DashboardView(TemplateView):

    template_name = 'journal/dashboard.html'

    def get(self, request):
        """Returns the home page"""
        learning_obj_requirements = '3,3,3,3,3,3,3,3'.split(',')
        learning_obj_completion = '0,1,2,3,4,5,6,7'.split(',')
        progress = list(map(lambda x, y: str(min(int(100 * (int(x) / int(y))), 100)),
                            learning_obj_completion,
                            learning_obj_requirements))
        print(progress)
        return render(request, self.template_name,
                      {'name': 'Bob', 'progress': progress})

class DashboardJSONView(View):

    def get(self, request):
        """Gets the associated JSON for the Category types. Will return a 404
        a non-valid category is given"""

        # The learning_objectives and cas have a split because items from the
        # db are represented as a string of ints with commas. This is only for
        # mocking purposes. Actual db fetching will be implemented later.
        dashboard_items = {
            'name': 'Bob',
            'learning_objectives': '0,1,2,3,4,5,6,7'.split(','),
            # 'learning_objectives': '0,0,0,0,0,0,0,0'.split(','),
            'cas': '0,1,2'.split(','),
            # 'cas': '0,0,0'.split(',')
            'requirements': {
                    'learning_objectives': '3,3,3,3,3,3,3,3'.split(','),
                    'cas': '1,1,1'.split(',')
                }
            }
        return JsonResponse(dashboard_items)
