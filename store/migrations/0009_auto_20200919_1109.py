# Generated by Django 3.0.8 on 2020-09-19 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_auto_20200918_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fullorder',
            name='name',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AddField(
            model_name='fullorder',
            name='address_line1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='address_line2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='recepient_fullname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fullorder',
            name='zipcode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Purchased_item',
        ),
    ]
