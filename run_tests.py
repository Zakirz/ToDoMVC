import os
import pytest

from Core.BrowserHelpers import BrowserHelpers


class RunTests(BrowserHelpers):
    def __init__(self):
        self.init_logger()
        try:
            pytest.main([
                "-s", "-v", f"{os.getcwd()}\\UI_Tests",
                "--html=" + self.HTML_REPORT_FILE,
                "--junit-xml=" + self.XML_REPORT_FILE
            ])
        finally:
            self.info_log("Test Completed")


if __name__ == '__main__':
    RunTests()
