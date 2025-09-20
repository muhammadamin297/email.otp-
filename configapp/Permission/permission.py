from django.core.cache import cache
from rest_framework.permissions import BasePermission

class IsEmailVerified(BasePermission):
    message = "Avval emailingizni verify qiling!"

    def has_permission(self, request, view):
        email = request.data.get("email") or request.query_params.get("email")
        if not email:
            return False
        return cache.get(f"{email}_verified", False)
