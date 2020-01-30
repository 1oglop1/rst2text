from pathlib import Path

from docutils.core import publish_parts, publish_doctree, publish_string
from rst2text.writers import HTMLWriter, TextWriter


class RstDocument:
    def __init__(self, file_name, settings=None):
        self.input_file = Path(file_name)

        self._config = None
        self._rst = None
        self._myrst = None

        # self.settings = {'initial_header_level': 2}
        self.settings = settings or {}

        with open(self.input_file) as inf:
            self.raw = inf.read()

    @property
    def rst(self):
        if not isinstance(self._rst, dict):
            htmlrst = publish_parts(
                source=self.raw, writer=HTMLWriter(), settings_overrides=self.settings
            )
            self._rst = htmlrst
        return self._rst

    @property
    def myrst(self):

        if not isinstance(self._myrst, dict):
            self._myrst = publish_parts(
                source=self.raw, writer=TextWriter(), settings_overrides=self.settings
            )

        # doctree = publish_doctree(
        #     source=self.raw,
        #     settings_overrides=self.settings
        # )
        return self._myrst
