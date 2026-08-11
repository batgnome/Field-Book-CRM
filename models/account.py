from dataclasses import dataclass

class Account:
    account_id: int
    company: str
    primary_contact_id: int | None
    status_id: int | None
    status: str | None
    address_id: int | None