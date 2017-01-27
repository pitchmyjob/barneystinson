from rest_framework import status
from rest_framework.reverse import reverse

from apps.authentication.factories import UserProFactory
from apps.core.api import tests

from .serializers import ProSerializer
from ..factories import ProFactory


class ProAPITestCase(tests.RetrieveAPITestCaseMixin,
                     tests.UpdateAPITestCaseMixin,
                     tests.DestroyAPITestCaseMixin,
                     tests.BaseAPITestCase):
    factory_class = ProFactory
    user_factory_class = UserProFactory
    serializer_class = ProSerializer

    def get_url(self):
        return reverse('pro')

    def get_retrieve_url(self):
        return self.get_url()

    def get_update_url(self):
        return self.get_url()

    def get_destroy_url(self):
        return self.get_url()

    def test_retrieve_not_logged_in_status_code(self):
        self.object = self.generate_object()
        response = self.get_retrieve_response()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_logged_in_related_pro_status_code(self):
        self.user = self.generate_user()
        self.client.force_authenticate(self.user)
        self.object = self.user.pro
        response = self.get_retrieve_response()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_logged_in_related_pro_content_returned(self):
        self.user = self.generate_user()
        self.client.force_authenticate(self.user)
        self.object = self.user.pro
        serializer = self.get_serializer(self.object)
        response = self.get_retrieve_response()
        self.assertEqual(response.data, serializer.data)

    def test_update_not_logged_in_status_code(self):
        self.object = self.generate_object()
        response = self.get_update_response(data={'company': 'New company'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_logged_in_related_pro_status_code(self):
        self.user = self.generate_user()
        self.client.force_authenticate(self.user)
        self.object = self.user.pro
        response = self.get_update_response(data={'company': 'New company'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_logged_in_related_pro_content_returned(self):
        self.user = self.generate_user()
        self.client.force_authenticate(self.user)
        self.object = self.user.pro
        response = self.get_update_response(data={'company': 'New company'})
        self.object.refresh_from_db()
        serializer = self.get_serializer(self.object)
        self.assertEqual(response.data, serializer.data)

    def test_destroy_not_logged_in_status_code(self):
        self.object = self.generate_object()
        response = self.get_destroy_response()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_destroy_logged_in_related_pro_status_code(self):
        self.user = self.generate_user()
        self.client.force_authenticate(self.user)
        self.object = self.user.pro
        response = self.get_destroy_response()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_destroy_logged_in_related_pro_is_active_pro(self):
        self.user = self.generate_user()
        self.client.force_authenticate(self.user)
        self.object = self.user.pro
        self.get_destroy_response()
        self.object.refresh_from_db()
        self.assertFalse(self.object.is_active)

    def test_destroy_logged_in_related_pro_is_active_user(self):
        self.user = self.generate_user()
        self.client.force_authenticate(self.user)
        self.object = self.user.pro
        self.get_destroy_response()
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)
