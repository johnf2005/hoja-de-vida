from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create or update the admin user for the application'

    def handle(self, *args, **options):
        username = 'adminjohn'
        email = 'admin@hojadevida.com'
        password = 'admin123456'

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'is_staff': True,
                'is_superuser': True,
            }
        )

        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'✅ Superuser "{username}" creado exitosamente')
            )
        else:
            # Asegurar que tenga permisos correctos
            if not user.is_staff or not user.is_superuser:
                user.email = email
                user.is_staff = True
                user.is_superuser = True
                user.set_password(password)
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Permisos de "{username}" actualizados')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'ℹ️  Usuario "{username}" ya existe con permisos correctos')
                )
