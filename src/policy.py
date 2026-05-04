from typing import Dict, List
from src.iam_models import ROLE_CATALOG, User


class AuthorizationError(Exception):
    pass


def build_user_from_claims(claims: Dict) -> User:
    roles = [ROLE_CATALOG.get(role_name, ROLE_CATALOG["Employee"]) for role_name in claims.get("roles", [])]
    return User(user_id=claims["sub"], username=claims["sub"], roles=roles)


def authorize(user: User, required_permissions: List[str]) -> bool:
    if not required_permissions:
        return True

    satisfied = [user.has_permission(permission) for permission in required_permissions]
    if not all(satisfied):
        missing = [permission for permission, ok in zip(required_permissions, satisfied) if not ok]
        raise AuthorizationError(f"User lacks required permissions: {missing}")

    return True


def evaluate_access(token_claims: Dict, required_permissions: List[str]) -> bool:
    user = build_user_from_claims(token_claims)
    return authorize(user, required_permissions)
