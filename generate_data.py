# generate_data.py
import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from clients.models import Client

def create_fake_clients(n=50):
    fake = Faker()
    products = [choice[0] for choice in Client.PRODUCT_CHOICES]
    statuses = [choice[0] for choice in Client.STATUS_CHOICES]
    market_shares = [choice[0] for choice in Client.MARKET_SHARE_CHOICES]
    countries = ['Poland', 'Germany', 'France', 'Spain', 'Italy', 'UK', 'Netherlands', 'Sweden']

    last_actions = [
        "Followed up on a recent meeting.",
        "Sent a product brochure via email.",
        "Had a discovery call to assess needs.",
        "Presented a demo of Product A.",
        "Scheduled a follow-up meeting for next week."
    ]

    next_actions = [
        "Send a custom proposal to the client.",
        "Schedule a technical call with the engineering team.",
        "Follow up on the last proposal sent.",
        "Conduct market research for potential expansion.",
        "Check in with the client to discuss recent feedback."
    ]

    roadblocks = [
        "Decision is pending due to budget review.",
        "Key stakeholder is on vacation.",
        "Technical integration requires more information.",
        "Client is considering other solutions.",
        "Project timeline has been postponed."
    ]

    comments = [
        "Client seems very interested in new features.",
        "The team is currently reviewing our last offer.",
        "Potential for a large contract next quarter.",
        "The client has a long sales cycle.",
        "The client is a key account with high priority."
    ]

    roadblocks = [choice[0] for choice in Client.ROADBLOCK_CHOICES] # Nowa lista opcji


    Client.objects.all().delete()
    print("Usunięto stare dane.")

    for _ in range(n):
        status = random.choice(statuses)
        roadblock = random.choice(roadblocks) if status == 'On Hold' else None

        Client.objects.create(
            company_name=fake.company(),
            country=random.choice(countries),
            contact_person=fake.name(),
            system_user=random.choice([True, False]),
            status=status,
            reason_for_roadblock=roadblock,
            offered_product=random.choice(products),
            potential_market_share=random.choice(market_shares),
            potential_yearly_sales=random.randint(1000, 500000), # Użycie randint dla liczb całkowitych
            last_action=random.choice(last_actions),
            next_action=random.choice(next_actions),
            comment_feedback=random.choice(comments)
        )
        print(f"Utworzono klienta numer {_ + 1}")

if __name__ == '__main__':
    print("Generowanie fikcyjnych danych...")
    create_fake_clients()
    print("Generowanie zakończone.")