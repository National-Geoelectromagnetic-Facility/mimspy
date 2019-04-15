# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""


class DownloadController:

    def __init__(self):
        self._files = {}
        self._download_file = []
        self._current_file = ''
        self._file_blocks_list = []
        self._save_directory = ''
        self._prog_total = 100
        self._prog = 1

    def push(self, files):
        for f in files:
            if f not in self._download_file:
                self._download_file.append(f)
        self._load_file()

    def _load_file(self):
        if len(self._file_blocks_list) == 0:
            self._current_file = self._download_file.pop(0)
            fs = int(self._files[self._current_file])
            self._file_blocks_list = [n for n in range(0, fs, 1024)]
            total_size = len(self._file_blocks_list)
            self._inc_value = 100 / total_size

    def save_dir(self, path):
        self._save_directory = path

    def card_files(self, fdic):
        self._files = fdic

    def file_block(self, block):
        if block is None:
            return (0, self._current_file.encode('utf-8'), b'\x00\x00')

        block_number = int.from_bytes(block[:4], 'big')
        block = block[4:]
        print(f'Block Number: {block_number}')
        if block_number == self._file_blocks_list[0]:
            self._file_blocks_list.pop(0)
            # TODO: Save blocks

        # print(block_number)
        if len(self._file_blocks_list) == 0:
            return (100, None, None)
        else:
            pos = (self._file_blocks_list[0]).to_bytes(4, 'big')
            # print(f'File Block List Length: {len(self._file_blocks_list)}')
            self._prog += self._inc_value
            return (self._prog, None, pos)
