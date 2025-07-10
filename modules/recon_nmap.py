"""Nmap recon module using python-nmap."""

import nmap

# TODO: Add functions to perform host scans

def scan_host(host):
    """Scan a host using nmap."""
    nm = nmap.PortScanner()
    # TODO: Handle exceptions and return structured results
    nm.scan(host)
    return nm[host]
