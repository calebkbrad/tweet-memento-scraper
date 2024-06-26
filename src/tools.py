#!/usr/bin/python3

from datetime import datetime

def get_memento_datetime(memento_datetime_header: str) -> datetime:
    """
    Extract appropriate datetime from Memento datetime header
    """
    return datetime.strptime(memento_datetime_header, "%a, %d %b %Y %H:%M:%S GMT")
