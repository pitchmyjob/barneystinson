class CurrentApplicantDefault(object):
    def set_context(self, serializer_field):
        self.applicant = serializer_field.context['request'].user.applicant

    def __call__(self):
        return self.applicant

    def __repr__(self):
        return unicode_to_repr('%s()' % self.__class__.__name__)
