from rest_framework import permissions


class IsAuthenticated(object):
    permission_classes = [permissions.IsAuthenticated]
