from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone


class CustomerManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  password=None, **extra_fields):
        user = self.create_user(username, password=password, **extra_fields)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, verbose_name='Логин')
    first_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Фамилия')

    is_active = models.BooleanField(default=False, verbose_name='Активен')
    is_admin = models.BooleanField(default=False, verbose_name='Это админ')
    # Если True - то заказчик, иначе флилансер
    is_customer = models.BooleanField(default=False, verbose_name='Заказчик')
    experience = models.SmallIntegerField(default=0, verbose_name='Опыт в годах')

    date_joined = models.DateTimeField(
        'Дата регистрации',
        default=timezone.now
    )

    USERNAME_FIELD = 'username'

    objects = CustomerManager()

    def __str__(self) -> str:
        return f'{self.username} {self.is_active} : {self.is_customer}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
