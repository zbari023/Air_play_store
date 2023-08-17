import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from faker import Faker
import random
from products.models import Products





def seed_product(n):
    fake = Faker()
    images = ['p1.png','p2.png','p3.png','p4.png','p5.png','p6.png']
    for x in range(n):
        Products.objects.create(
            name = fake.name(),
            price = round(random.uniform(200.99 , 999.99),2),
            image = f'products/{images[random.randint(0,5)]}'
        )
    print(f'{n} products was successfuly')
            
    
        
        
        
seed_product(2)