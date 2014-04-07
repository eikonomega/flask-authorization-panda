"""
**Flask-Authorization-Panda provides easy loading and access to the data elements of
JSON based configuration files.**

Usage
-----

Assuming that an environment variable 'SHARED_CONFIG_FILES' exists
and points to a directory containing multiple JSON files, including
the following::

    ldap.json
      {
        "primary": {
            "url": "ldaps://primaryldap.example.edu:111",
            "login": "cn=LDAP Testing",
            "password": "LDAP Password"
        }
      }

    smtp.json
      {
        "TestAccount1": {
            "url": "smtp.yourschool.edu",
            "login": "testaccount1",
            "password": "testaccount1password"
        }
      }

You would access the contents of those configuration files like this::

    >>> from configuration_panda import ConfigurationPanda
    >>> program_settings = ConfigurationPanda(['SHARED_CONFIG_FILES'])
    >>> program_settings.ldap['primary']['url']
    ldaps://primaryldap.example.edu:111
    >>> program_settings.smtp['TestAccount1']['login']
    testaccount1

Or, if you prefer dictionary-style syntax::

    >>> from configuration_panda import ConfigurationPanda
    >>> program_settings = ConfigurationPanda(['SHARED_CONFIG_FILES'])
    >>> program_settings['ldap']['primary']['url']
    ldaps://primaryldap.example.edu:111
    >>> program_settings['smtp']['TestAccount1']['login']
    testaccount1


"""

__version__ = '0.5'

from basic_auth import basic_auth