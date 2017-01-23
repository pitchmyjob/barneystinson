from apps.core.api import tests

from apps.authentication.factories import UserProFactory

from .serializers import ProSerializer
from ..factories import ProFactory


class ProAPITestCase(tests.RetrieveAPITestCaseMixin, tests.BaseAPITestCase):
    base_name = 'pro'
    factory_class = ProFactory
    user_factory_class = UserProFactory
    serializer_class = ProSerializer

    def get_retrieve_objet_id(self):
        return self.user.pro.pk

    def generate_retrieve_object(self):
        return self.user.pro
