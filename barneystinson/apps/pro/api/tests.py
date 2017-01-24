from rest_framework import status

from apps.authentication.factories import UserProFactory
from apps.core.api import tests

from .serializers import ProSerializer
from ..factories import ProFactory


class ProAPITestCase(tests.RetrieveAPITestCaseMixin,
                     tests.UpdateAPITestCaseMixin,
                     tests.DestroyAPITestCaseMixin,
                     tests.BaseAPITestCase):
    base_name = 'pro'
    factory_class = ProFactory
    user_factory_class = UserProFactory
    serializer_class = ProSerializer
    retrieve_status_code_only = True
    retrieve_expected_status_code = status.HTTP_401_UNAUTHORIZED

    def test_authenticated_only_related_pro_status_code(self):
        self.authenticate_user()
        self.object = self.generate_object()
        response = self.get_retrieve_response()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authenticated_realted_pro_status_code(self):
        self.authenticate_user()
        self.object = self.user.pro
        response = self.get_retrieve_response()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_content_returned(self):
        self.authenticate_user()
        self.object = self.user.pro
        serializer = self.get_serializer(self.object)
        response = self.get_retrieve_response()
        self.assertEqual(response.data, serializer.data)
