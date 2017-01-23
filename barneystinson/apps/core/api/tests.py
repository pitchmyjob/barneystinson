from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from django.core.exceptions import ImproperlyConfigured
from django.utils.six import text_type


class BaseAPITestCase(APITestCase):
    base_name = None
    factory_class = None
    user_factory_class = None
    serializer_class = None
    lookup_field = 'pk'

    def get_factory_class(self):
        return getattr(self, 'factory_class')

    def get_object(self, factory, **kwargs):
        return factory.create(**kwargs)

    def generate_object(self, **kwargs):
        return self.get_object(self.get_factory_class(), **kwargs)

    def get_user_factory_class(self):
        return getattr(self, 'user_factory_class')

    def get_user(self, factory, **kwargs):
        return factory.create(**kwargs)

    def generate_user(self, **kwargs):
        return self.get_user(self.get_user_factory_class(), **kwargs)

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

    def setUp(self):
        if self.user_factory_class:
            self.user = self.generate_user()
            self.client.force_authenticate(self.user)


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

        identical = len(response.data) == len(serializer.data)
        if identical:
            for obj in serializer.data:
                if obj not in response.data:
                    identical = False
        self.assertEqual(identical, True)


class RetrieveAPITestCaseMixin(object):
    RETRIEVE_SUFFIX_URL = '-detail'

    def get_retrieve_objet_id(self):
        return getattr(self.object, self.lookup_field)

    def get_retrieve_url(self):
        object_id = self.get_retrieve_objet_id()
        return reverse(self.base_name + self.RETRIEVE_SUFFIX_URL, args=[text_type(object_id)])

    def get_retrieve_response(self, **kwargs):
        return self.client.get(self.get_retrieve_url(), **kwargs)

    def generate_retrieve_object(self):
        return self.generate_object()

    def test_retrieve_status_code(self, **kwargs):
        self.object = self.generate_object()

        response = self.get_retrieve_response(**kwargs)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_retrieve_returned_data(self, **kwargs):
        self.object = self.generate_retrieve_object()

        serializer = self.get_serializer(self.object)
        response = self.get_retrieve_response(**kwargs)
        self.assertEqual(response.data, serializer.data)
