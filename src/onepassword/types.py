"""
Generated by typeshare 1.9.2
"""

from __future__ import annotations

from pydantic import BaseModel
from typing import List, Literal, Optional


class Item(BaseModel):
    id: str
    title: str
    category: ItemCategory
    vault_id: str
    fields: List[ItemField]
    sections: List[ItemSection]


ItemCategory = Literal[
    "Login",
    "SecureNote",
    "CreditCard",
    "CryptoWallet",
    "Identity",
    "Password",
    "Document",
    "ApiCredentials",
    "BankAccount",
    "Database",
    "DriverLicense",
    "Email",
    "MedicalRecord",
    "Membership",
    "OutdoorLicense",
    "Passport",
    "Rewards",
    "Router",
    "Server",
    "SshKey",
    "SocialSecurityNumber",
    "SoftwareLicense",
    "Person",
    "Unsupported",
]


class ItemField(BaseModel):
    id: str
    title: str
    section_id: Optional[str]
    field_type: ItemFieldType
    value: str


ItemFieldType = Literal["Text", "Concealed", "Unsupported"]


class ItemSection(BaseModel):
    id: str
    title: str
