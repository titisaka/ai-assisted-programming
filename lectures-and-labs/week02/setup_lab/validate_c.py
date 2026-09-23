"""Practical email-address validation."""

import re


_EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"
    r"(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"@"
    r"[A-Za-z0-9]"
    r"(?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+"
)


def validate_email(address: str) -> bool:
    """Return whether *address* has a practical email-address format."""
    if not isinstance(address, str) or len(address) > 254:
        return False

    return _EMAIL_PATTERN.fullmatch(address) is not None
