"""SMB operations module."""

# Optional dependency
try:
    import smbclient
except ImportError:  # pragma: no cover - optional
    smbclient = None

# TODO: Add SMB share enumeration and file listing

def list_shares(host):
    """List SMB shares on a host."""
    if not smbclient:
        raise RuntimeError('smbclient module not available')
    return smbclient.list_shares(host)
