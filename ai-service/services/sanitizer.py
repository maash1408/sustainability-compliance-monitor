import bleach


def sanitize_text(text: str):
    if not text:
        return ""

    return bleach.clean(text, tags=[], strip=True)