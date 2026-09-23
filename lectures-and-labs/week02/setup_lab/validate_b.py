"""Deliberately simple email-address validation."""


def validate_email(address: str) -> bool:
    """Return whether *address* contains an @ and a later dot."""
    if not isinstance(address, str) or len(address) > 254:
        return False

    at = address.find("@")
    return at >= 0 and "." in address[at + 1:]
