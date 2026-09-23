"""Simple email-address validation."""

import re


def validate_email(address: str) -> bool:
    """Return whether *address* has a plausible email format."""
    if not isinstance(address, str) or len(address) > 254:
        return False

    return re.fullmatch(
        r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
        r"@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
        r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+",
        address,
    ) is not None
