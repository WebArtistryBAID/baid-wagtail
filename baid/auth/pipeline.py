def grant_wagtail_access(backend, user, response, *args, **kwargs):
    user.is_staff = True
    user.is_superuser = True
    user.save()
