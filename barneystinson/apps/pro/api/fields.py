from rest_framework.compat import unicode_to_repr


class CurrentProDefault(object):
    def set_context(self, serializer_field):
        self.pro = serializer_field.context['request'].user.pro

    def __call__(self):
        return self.pro

    def __repr__(self):
        return unicode_to_repr('%s()' % self.__class__.__name__)
