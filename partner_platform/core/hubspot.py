import requests
from django.conf import settings

def sync_partner_to_hubspot(partner):
    url = f"https://{settings.HUBSPOT_BASE_URL}/crm/v3/objects/companies"
    headers = {
        "Authorization": f"Bearer {settings.HUBSPOT_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "properties": {
            "name": partner.name,
            "country": partner.country,
            "monthly_usage": partner.monthly_usage
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    return response.json()["id"]
