"""
Settings for the challenges application
"""

"""
Disable or enable presentation mode. Use this if you want to host a CTF event.
If enabled:
- Do not show accounts with author rights in the high score
- Do not show a notification for normal users that they might get author rights
"""
PRESENTATION_MODE = False

"""
Disable the creation of new users and only show challenges etc. to logged in users.
"""
RESTRICTED_MODE = False

HOST_NAME = 'localhost'