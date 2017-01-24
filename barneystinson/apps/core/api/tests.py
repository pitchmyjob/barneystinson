import unittest

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from django.core.exceptions import ImproperlyConfigured
from django.utils.six import text_type


class BaseAPITestCase(APITestCase):
    LIST_SUFFIX_URL = '-list'
    DETAIL_SUFFIX_URL = '-detail'
    LOOKUP_FIELD = 'pk'

    base_name = None
    factory_class = None
    serializer_class = None
    user_factory_class = None

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

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def authenticate_user(self):
        self.user = self.generate_user()
        self.client.force_authenticate(self.user)


class ListAPITestCaseMixin(object):
    nb_objects_to_generate = 5
    list_status_code_only = False
    list_expected_status_code = status.HTTP_200_OK

    def get_list_url(self):
        return reverse(self.base_name + self.LIST_SUFFIX_URL)

    def get_list_response(self, **kwargs):
        return self.client.get(self.get_list_url(), **kwargs)

    def generate_objects(self, **kwargs):
        return [self.generate_object(**kwargs) for i in range(self.nb_objects_to_generate)]

    def test_list_status_code(self):
        response = self.get_list_response()
        self.assertEqual(response.status_code, self.list_expected_status_code)

    def test_list_nb_data_returned(self):
        if self.list_status_code_only:
            return unittest.skip('`list_status_code_only` attribut set to True')

        data = self.generate_objects()
        response = self.get_list_response()
        self.assertTrue(len(response.data) == len(data))

    def test_list_content_returned(self):
        if self.list_status_code_only:
            return unittest.skip('`list_status_code_only` attribut set to True')

        data = self.generate_objects()
        response = self.get_list_response()
        serializer = self.get_serializer(data, many=True)

        is_identical = len(response.data) == len(serializer.data)
        if is_identical:
            for obj in response.data:
                if obj not in serializer.data:
                    is_identical = False
                    break
        self.assertTrue(is_identical)


class RetrieveAPITestCaseMixin(object):
    retrieve_status_code_only = False
    retrieve_expected_status_code = status.HTTP_200_OK

    def get_retrieve_url(self):
        object_id = getattr(self.object, self.LOOKUP_FIELD)
        return reverse(self.base_name + self.DETAIL_SUFFIX_URL, args=[text_type(object_id)])

    def get_retrieve_response(self, **kwargs):
        return self.client.get(self.get_retrieve_url(), **kwargs)

    def test_retrieve_status_code(self):
        self.object = self.generate_object()
        response = self.get_retrieve_response()
        self.assertEqual(response.status_code, self.retrieve_expected_status_code)

    def test_retrieve_content_returned(self):
        if self.retrieve_status_code_only:
            return unittest.skip('`retrieve_status_code_only` attribut set to True')

        self.object = self.generate_object()
        serializer = self.get_serializer(self.object)
        response = self.get_retrieve_response()
        self.assertEqual(response.data, serializer.data)


class CreateAPITestCaseMixin(object):
    def get_create_data(self):
        pass

    def get_create_url(self):
        pass

    def get_create_response(self, data=None, **kwargs):
        pass

    def get_lookup_from_response(self, data):
        pass

    def test_create(self, data=None, **kwargs):
        pass


class UpdateAPITestCaseMixin(object):
    def get_update_url(self):
        pass

    def get_update_response(self, data=None, results=None, use_path=None, **kwargs):
        pass

    def get_update_data(self):
        pass

    def get_update_results(self, data=None):
        pass

    def get_relationship_value(self, related_obj, key):
        pass

    def test_update(self, data=None, results=None, use_patch=None, **kwargs):
        pass


class DestroyAPITestCaseMixin(object):
    def get_destroy_url(self):
        pass

    def get_destroy_response(self, **kwargs):
        pass

    def test_destroy(self, **kwargs):
        pass
