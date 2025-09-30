import filetype
import mimetypes
import magic

def detect_type(filepath):
    # Précision maximale: d'abord via python-magic, puis filetype, puis mimetypes
    try:
        mime = magic.from_file(filepath, mime=True)
        desc = magic.from_file(filepath)
        return mime, desc
    except Exception:
        pass
    kind = filetype.guess(filepath)
    if kind:
        return kind.mime, kind.extension
    mime, encoding = mimetypes.guess_type(filepath)
    return mime or "application/octet-stream", "unknown"