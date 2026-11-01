from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def role_required(*allowed_roles):
    """
    Restrict a view to users belonging to the specified groups.

    Superusers have full application access.
    """
    def decorator(view_func):

        @login_required
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            user = request.user

            # Superusers have full access.
            if user.is_superuser:
                return view_func(request, *args, **kwargs)

            # Check the user's assigned groups.
            if user.groups.filter(
                name__in=allowed_roles
            ).exists():
                return view_func(request, *args, **kwargs)

            messages.error(
                request,
                "You do not have permission to access this page."
            )

            raise PermissionDenied

        return wrapper

    return decorator