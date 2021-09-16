from django.contrib.auth.models import User

def add_variable_to_context(request):
    created_users = User.objects.all()
    return {
        'created_users': created_users
    }

