import io
import unittest
from contextlib import redirect_stdout

from clinterpy.cli import main


class TestCli(unittest.TestCase):
    def test_main_prints_ready_message(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = main()

        self.assertEqual(code, 0)
        self.assertEqual(buffer.getvalue().strip(), "clinterpy is ready")
