from dataclasses import dataclass
from typing import List

@dataclass
class Role:
    name: str
    permissions: List[str]

@dataclass
class User:
    user_id: str
    username: str
    roles: List[Role]

    def has_permission(self, permission: str) -> bool:
        return any(permission in role.permissions for role in self.roles)

# Example role definitions for a demo architecture
ADMIN = Role(name="Admin", permissions=["read:data", "write:data", "manage:users", "deploy:infra"])
MANAGER = Role(name="Manager", permissions=["read:data", "write:data", "approve:requests"])
EMPLOYEE = Role(name="Employee", permissions=["read:data"])

ROLE_CATALOG = {
    "Admin": ADMIN,
    "Manager": MANAGER,
    "Employee": EMPLOYEE,
}
