""""
Test custom django management commands
"""

from unittest.mock import patch

from psycopg2 import OperationalError as psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """ Test command ."""
    def test_wait_for_db_ready(self, patched_check):
        """ Test waiting for database if database is ready"""
        patched_check.return_value = True
        """ when check is called we only want to return a value"""
        call_command('wait_for_db')
        """ check if the database is set correctly and can be called"""

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def wait_for_db_delay(self, patched_sleep, patched_check):
        """ Test waiting for the database when getting OperationalError"""
        patched_check.side_effect = [psycopg2Error] * 2 + \
            [OperationalError]*3 + [True]
        """ determines how many times it tries to connect and finds error, on
        the 6th, should True"""
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
