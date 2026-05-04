from src.auth import create_access_token, decode_access_token, TokenError
from src.policy import evaluate_access


def run_demo():
    print("=== Solution Architect + IAM Engineer Demo ===")
    print("Creating a token for an Admin user")
    token = create_access_token(subject="alice@example.com", roles=["Admin"])
    print(f"Generated token: {token}\n")

    try:
        claims = decode_access_token(token)
        print(f"Decoded claims: {claims}\n")

        required_permissions = ["deploy:infra", "manage:users"]
        print(f"Evaluating access for permissions: {required_permissions}")
        if evaluate_access(claims, required_permissions):
            print("Access granted: user is authorized for the requested operation.")
    except TokenError as exc:
        print(f"Authentication failed: {exc}")
    except Exception as exc:
        print(f"Authorization failed: {exc}")


if __name__ == "__main__":
    run_demo()
