from apps.core.api.pagination import CustomPagination, CustomCursorPagination


class CandidacyListPagination(CustomPagination):
    page_size = 10


class CandidacyCommentsPagination(CustomCursorPagination):
    page_size = 6
