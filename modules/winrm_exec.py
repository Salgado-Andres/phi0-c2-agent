"""WINRM remote command execution module."""

# Optional dependency
try:
    import winrm
except ImportError:  # pragma: no cover - optional
    winrm = None

# TODO: Implement WINRM command execution

def run_command(host, username, password, command):
    """Run a remote command via WINRM."""
    if not winrm:
        raise RuntimeError('winrm module not available')
    session = winrm.Session(host, auth=(username, password))
    return session.run_cmd(command)
