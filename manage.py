#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangogirl.settings")
>>>>>>> 58b79890669009e69b4541e50f4c72a82e7bcfff

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
