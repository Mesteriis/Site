# Generated by Django 2.2.13 on 2020-07-09 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTimeStart', models.DateTimeField(auto_now_add=True, verbose_name='Дата постановки')),
                ('dateTimeEnd', models.DateTimeField(auto_now_add=True, verbose_name='Сдалать до')),
                ('isImportant', models.BooleanField(default=False, verbose_name='Важное')),
                ('title', models.TextField(default='Заголовок уведомления', max_length=120)),
                ('text', models.TextField(default='Текст уведомления', max_length=500)),
                ('isCompleted', models.BooleanField(default=False, verbose_name='Выполнена')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Задача для пользователя',
                'verbose_name_plural': 'Задачи для пользователя',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('isDialer', models.BooleanField(blank=True, default=False)),
                ('isAllowSubDealer', models.BooleanField(default=False)),
                ('isFinanceBlock', models.BooleanField(default=False)),
                ('comments', models.TextField(blank=True, max_length=500)),
                ('personalSettingsSite', jsonfield.fields.JSONField(default={'dashC': {'colorThem': 'white'}, 'dashS': {'activeModule': {'corpMessage': False, 'searchPanel': False}, 'interfacesStyle': {'SizeText': {'Footer': False, 'body': False, 'navBar': False, 'sideBar': False}, 'colorThem': {'brand': '#007bff', 'navBar': '#007bff', 'sidebar': {'Them': 'dark', 'color': '#007bff'}}, 'styleSideBar': {'childIndent': False, 'compact': False, 'flat': False, 'legacy': False}}}})),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='userprofile/avatar/')),
                ('wialonToken', models.TextField(blank=True, max_length=100)),
                ('omnikomToken', models.TextField(blank=True, max_length=100)),
                ('isSupportChat', models.BooleanField(default=False, verbose_name='Специалист ТП, доступ в чат')),
                ('isSupportChatOnlineStatus', models.CharField(choices=[('ol', 'В Сети'), ('of', 'Вне Сети'), ('bs', 'Отсутствует'), ('bc', 'Занят с клиентом')], default='ol', max_length=2, verbose_name='Статус сотрудника в Чате')),
                ('redirect_url_login', models.URLField(blank=True, max_length=255, verbose_name='Ссылка после удачного логина')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль для пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время получения')),
                ('isMarkRead', models.BooleanField(default=False)),
                ('title', models.TextField(default='Заголовок уведомления', max_length=120)),
                ('text', models.TextField(default='Текст уведомления', max_length=500)),
                ('link', models.URLField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Уведомление для пользователя',
                'verbose_name_plural': 'Уведомления для пользователя',
            },
        ),
        migrations.CreateModel(
            name='keyChanters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_login', models.CharField(default='test1', max_length=20, verbose_name='Логин к Wialon')),
                ('w_password', models.CharField(default='test1', max_length=20, verbose_name='Пароль к Wialon')),
                ('o_login', models.CharField(default='demo', max_length=20, verbose_name='Логин к Omnicomm')),
                ('o_password', models.CharField(default='demo', max_length=20, verbose_name='Пароль к Оmnicomm')),
                ('isBlockWialon', models.BooleanField(default=False)),
                ('isBlockOmnicom', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
