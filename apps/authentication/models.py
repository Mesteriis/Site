from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
import jsonfield


class Firm(models.Model):
    pass


defaultSettings = {
    'dashC': {
        'colorThem': 'white',
    },
    'dashS': {
        'activeModule': {
            'searchPanel': False,
            'corpMessage': False,
        },
        'interfacesStyle': {
            'SizeText': {
                'body': False,
                'navBar': False,
                'sideBar': False,
                'Footer': False,
            },
            'styleSideBar': {
                'flat': False,
                'legacy': False,
                'compact': False,
                'childIndent': False,
            },
            'colorThem': {
                'navBar': '#007bff',
                'sidebar': {
                    'Them': 'dark',
                    'color': '#007bff',
                },
                'brand': '#007bff'
            }
        },
    }
}


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # firmID = models.OneToOneField(Firm, on_delete=models.CASCADE,  blank=True)
    # module = models // FIXME подумать
    isDialer = models.BooleanField(default=False, blank=True)
    isAllowSubDealer = models.BooleanField(default=False)
    isFinanceBlock = models.BooleanField(default=False)
    comments = models.TextField(max_length=500, blank=True)
    # personalSettingsSite = models.TextField(default=defaultSettings)
    personalSettingsSite = jsonfield.JSONField(default=defaultSettings)
    avatar = models.ImageField(
        upload_to='userprofile/avatar/',
        blank=True,
        null=True
    )

    wialonToken = models.TextField(max_length=100, blank=True)
    omnikomToken = models.TextField(max_length=100, blank=True)
    isSupportChat = models.BooleanField(default=False, verbose_name="Специалист ТП, доступ в чат")
    ONLINE = 'ol'
    OFFLINE = 'of'
    BUSY = 'bs'
    BUSY_Client = 'bc'
    typesStatus = (
        (ONLINE, 'В Сети'),
        (OFFLINE, 'Вне Сети'),
        (BUSY, 'Отсутствует'),
        (BUSY_Client, 'Занят с клиентом'),
    )
    isSupportChatOnlineStatus = models.CharField(max_length=2, choices=typesStatus, default=ONLINE,
                                                 verbose_name="Статус сотрудника в Чате")
    redirect_url_login = models.URLField(max_length=255, blank=True, verbose_name="Ссылка после удачного логина")

    def __str__(self):
        return '%s из %s' % (self.user, self.location)

    class Meta:
        verbose_name = 'Профиль для пользователя'
        verbose_name_plural = 'Профили пользователей'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        keyChanters.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    # instance.keyChanters.save()


class keyChanters(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    w_login = models.CharField(max_length=20, verbose_name='Логин к Wialon', default='test1')
    w_password = models.CharField(max_length=20, verbose_name='Пароль к Wialon', default='test1')
    o_login = models.CharField(max_length=20, verbose_name='Логин к Omnicomm', default='demo')
    o_password = models.CharField(max_length=20, verbose_name='Пароль к Оmnicomm', default='demo')
    isBlockWialon = models.BooleanField(default=False)
    isBlockOmnicom = models.BooleanField(default=False)


# @receiver(post_save, sender=User)
# def create_user_keyChanters(sender, instance, created, **kwargs):
#     if created:
#         keyChanters.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_keyChanters(sender, instance, **kwargs):
#     instance.keyChanters.save()


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время получения')
    isMarkRead = models.BooleanField(default=False)
    title = models.TextField(max_length=120, blank=False, default='Заголовок уведомления')
    text = models.TextField(max_length=500, blank=False, default='Текст уведомления')
    link = models.URLField(blank=True)

    def __str__(self):
        return '%s / %s' % (self.user, self.title)

    class Meta:
        verbose_name = 'Уведомление для пользователя'
        verbose_name_plural = 'Уведомления для пользователя'


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateTimeStart = models.DateTimeField(auto_now_add=True, verbose_name='Дата постановки')
    dateTimeEnd = models.DateTimeField(auto_now_add=True, verbose_name='Сдалать до')
    isImportant = models.BooleanField(default=False, verbose_name='Важное')
    title = models.TextField(max_length=120, blank=False, default='Заголовок уведомления')
    text = models.TextField(max_length=500, blank=False, default='Текст уведомления')
    isCompleted = models.BooleanField(default=False, verbose_name='Выполнена')

    def __str__(self):
        return '%s / %s' % (self.user, self.title)

    class Meta:
        verbose_name = 'Задача для пользователя'
        verbose_name_plural = 'Задачи для пользователя'
