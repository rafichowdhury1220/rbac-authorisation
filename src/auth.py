import jwt
from datetime import datetime, timezone
from typing import Dict, List

SECRET_KEY = "super-secret-architect-key"
ALGORITHM = "HS256"

class TokenError(Exception):
    pass


def create_access_token(subject: str, roles: List[str], expires_in_seconds: int = 3600) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": subject,
        "roles": roles,
        "iat": int(now.timestamp()),
        "exp": int((now.timestamp() + expires_in_seconds)),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> Dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError as exc:
        raise TokenError("Token expired") from exc
    except jwt.PyJWTError as exc:
        raise TokenError("Invalid token") from exc

    if "sub" not in payload or "roles" not in payload:
        raise TokenError("Malformed token claims")

    return payload
