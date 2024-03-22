from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0003_job_search_vector'),
    ]

    operations = [
        migrations.RunSQL("CREATE INDEX job_search_vector_idx ON job_app_job USING gin(search_vector);"),
    ]