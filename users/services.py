from django.contrib.auth import authenticate, login, logout
from .models import User

class UserService:
    @staticmethod
    def register_user(username, email, password, role='student'):
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role
        )
        return user
    
    @staticmethod
    def authenticate_user(request, username, password):
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return user
        return None
    
    @staticmethod
    def logout_user(request):
        logout(request)
    
    @staticmethod
    def update_profile(user, **kwargs):
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        user.save()
        return user
    
    @staticmethod
    def get_all_users():
        return User.objects.all()
    
    @staticmethod
    def get_authors():
        return User.objects.filter(role='author')
