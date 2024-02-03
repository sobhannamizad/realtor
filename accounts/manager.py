from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,full_name,phone_number,password):
        if not full_name:
            raise ValueError('full name is required')
        if not phone_number:
            raise ValueError('phone number is required')
        if not password:
            raise ValueError('password is required')

        user = self.model(phone_number=phone_number,full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,full_name,phone_number,code,password):
        user =self.create_user(phone_number=phone_number,full_name=full_name,password=password)
        user.is_admin =True
        user.code =code
        user.save(using=self.db)
        return user
