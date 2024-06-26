from .core import _invoke
import json
from .types import Item


class Items:
    """Contains all operations the SDK client can perform on 1Password items."""

    def __init__(self, client_id):
        self.client_id = client_id

    async def create(self, item):
        """Create a new item"""
        response = await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "Create",
                    "parameters": {
                        "item": item.dict(),
                    },
                },
            }
        )
        result = Item(**json.loads(response))
        return result

    async def get(self, vault_id, item_id):
        """Get an item by vault and item ID"""
        response = await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "Get",
                    "parameters": {
                        "vault_id": vault_id,
                        "item_id": item_id,
                    },
                },
            }
        )
        result = Item(**json.loads(response))
        return result

    async def update(self, item):
        """Update an existing item. You can currently only edit text and concealed fields."""
        response = await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "Update",
                    "parameters": {
                        "item": item.dict(),
                    },
                },
            }
        )
        result = Item(**json.loads(response))
        return result

    async def delete(self, vault_id, item_id):
        """Delete an item. """
        await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "Delete",
                    "parameters": {
                        "vault_id": vault_id,
                        "item_id": item_id,
                    },
                },
            }
        )
