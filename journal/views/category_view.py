import csv
import os
from django.http import JsonResponse
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from django.views.generic import View

_CATEGORY_TYPES = ['cas', 'learning_objectives']
_CSV_FILE_DIR = os.path.join(os.getcwd(), 'journal', 'files')

class CategoryJSONView(View):

    def _get_categories_from_file(self, category):
        """
        Outputs a dictionary of the particular category type. CSV files
        are expected to have the following format:

        1,Creativity
        2,Action
        3,Service
        """
        category = str(category)
        assert category in _CATEGORY_TYPES, 'Category must be in approved \
                                            category types!'
        types = {}
        file_name = os.path.join(_CSV_FILE_DIR, '{0}.csv'.format(category))
        with open(file_name) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                types[row[0]] = row[1]
        return types


    def get(self, request, *args, **kwargs):
        """Gets the associated JSON for the Category types. Will return a 404
        a non-valid category is given"""
        assert kwargs['category'] != None, HttpResponseBadRequest(
            'Must provide category!')

        if kwargs['category'] in _CATEGORY_TYPES:
            result = self._get_categories_from_file(kwargs['category'])
            return JsonResponse(result)
        else:
            return HttpResponseNotFound('Category not found!')
