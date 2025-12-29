## Demo Project: Distributor–Partner Management with HubSpot Integration

This is a simplified demo project showcasing:
- Basic data modeling (Distributor / Partner)
- REST API design
- Third-party API integration with HubSpot CRM
- Django backend architecture
    ```
    ├── PostgreSQL (Source of Truth)
    │   ├── distributors
    │   └── partners
    │
    ├── REST APIs (CRUD)
    │
    └── HubSpot Sync (One-way)
        ├── Distributor → HubSpot Company
        └── Partner → HubSpot Company / Custom Object
    ```
  
Authentication is intentionally omitted to keep the demo publicly accessible.
In production, this would be secured using OIDC/JWT-based authentication.
