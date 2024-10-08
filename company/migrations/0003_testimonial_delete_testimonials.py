# Generated by Django 4.0.5 on 2024-05-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('actual_testimonial', models.TextField()),
                ('photos', models.ImageField(upload_to='testimonials/')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Testimonials',
        ),
    ]
