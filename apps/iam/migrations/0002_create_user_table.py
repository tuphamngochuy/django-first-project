from email.policy import default
from django.db import migrations, models
from django.db.models.fields import uuid
from apps.iam.migrations.common import utils

(is_anonymous_forwards, is_anonymous_backwards) = utils.generate_default_boolean_field_migration('"authentication"."user"', 'is_anonymous', True)
(created_at_forwards, created_at_backwards) = utils.generate_default_datetime_field_migration('"authentication"."user"', 'created_at')
(updated_at_forwards, updated_at_backwards) = utils.generate_default_datetime_field_migration('"authentication"."user"', 'updated_at')

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iam', '0001_create_authentication_schema'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)),
                ('created_at', models.DateTimeField(auto_now_add=True, editable=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True, editable=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
                ('display_name', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(null=True, blank=True, max_length=100)),
                ('salt', models.CharField(null=True, blank=True, max_length=100)),
                ('last_login_at', models.DateTimeField(blank=True, null=True)),
                ('is_anonymous', models.BooleanField()),
            ],
            options={
                'db_table': '"authentication"."user"',
                'managed': True
            },
        ),
        migrations.RunPython(is_anonymous_forwards, is_anonymous_backwards),
        *utils.add_base_field_default('"authentication"."user"'),    
    ]