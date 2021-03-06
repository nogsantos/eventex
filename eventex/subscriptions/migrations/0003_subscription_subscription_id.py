# Generated by Django 2.2.5 on 2019-10-08 03:07

from django.db import migrations, models
import uuid


def create_uuid(apps, schema_editor):
    subscriptions = apps.get_model('subscriptions', 'Subscription')
    for subscription in subscriptions.objects.all():
        subscription.referral_code = uuid.uuid4()
        subscription.save()


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20191008_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subscription_id',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name='subscription',
            name='subscription_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True)
        )
    ]
