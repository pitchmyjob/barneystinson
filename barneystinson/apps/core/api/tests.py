from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from django.core.exceptions import ImproperlyConfigured
from django.utils.six import text_type


class BaseAPITestCase(APITestCase):
    base_name = None
    factory_class = None
    serializer_class = None

    def get_factory_class(self):
        return getattr(self, 'factory_class')

    def get_user_factory_class(self):
        return getattr(self, 'user_factory_class')

    def get_object(self, factory):
        return factory.create()

    def generate_object(self):
        return self.get_object(self.get_factory_class())

    def get_serializer_class(self):
        if self.serializer_class is None:
            raise ImproperlyConfigured('"%s" should either include a `serializer_class` attribute,'
                                       'or override the `get_serializer_class()` method.' % self.__class__.__name__)
        return self.serializer_class

    def get_serializer_context(self):
        return {}

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class ListAPITestCaseMixin(object):
    LIST_SUFFIX_URL = '-list'
    pagination_results_field = None

    def get_list_url(self):
        return reverse(self.base_name + self.LIST_SUFFIX_URL)

    def get_list_response(self, **kwargs):
        return self.client.get(self.get_list_url(), **kwargs)

    def test_list_status_code(self, **kwargs):
        response = self.get_list_response(**kwargs)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_list_nb_returned_data(self, **kwargs):
        data = [self.generate_object() for i in range(5)]
        response = self.get_list_response(**kwargs)
        self.assertTrue(len(response.data) == len(data))

    def test_list_content_returned_data(self, **kwargs):
        data = [self.generate_object() for i in range(5)]
        response = self.get_list_response(**kwargs)
        serializer = self.get_serializer(data, many=True)

        identical = True
        for obj in response.data:
            if obj not in serializer.data:
                identical = False
        self.assertEqual(identical, True)
