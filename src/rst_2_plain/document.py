from pathlib import Path

from docutils.core import publish_parts, publish_doctree, publish_string
from rst_2_plain.writers import HTMLWriter, TextWriter


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
        doc_pp = publish_parts(source=self.raw)
        doc_tree = publish_doctree(self.raw)
        # text_writer =
        # writer =

        if not isinstance(self._rst, dict):
            self._myrst = publish_parts(source=self.raw,
                                        writer=HTMLWriter(),
                                        settings_overrides=self.settings)

            self._rst = publish_parts(source=self.raw,
                                      writer=TextWriter(),
                                      settings_overrides=self.settings)

            print(self._rst)
        return self._rst
