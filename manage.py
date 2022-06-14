#!/usr/bin/env python

import os
import sys
from django.http import  Http404


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sherzamon_uz.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
               Http404
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
