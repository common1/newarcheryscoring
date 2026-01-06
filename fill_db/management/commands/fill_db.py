import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from userauth.models import CustomUser
from django.utils import lorem_ipsum

class Command(BaseCommand):
    user = None   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # get or create superuser
        self.user = CustomUser.objects.filter(username='admin').first()
        if not self.user:
            self.user = CustomUser.objects.create_superuser(
                username='admin',
                # display_name='Admin User',
                password='changeme', 
                email='me@mail.com'
            )
        self.stdout.write(self.style.SUCCESS('Superuser "admin" ensured.'))
        
    help = 'Populate the database with sample data'
    
    def handle(self, *args, **kwargs):
        pass
