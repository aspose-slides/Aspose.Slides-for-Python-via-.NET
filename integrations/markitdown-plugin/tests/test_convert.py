import os
import shutil

from unittest import TestCase
from aspose_slides_markitdown_plugin import AsposeSlidesConverter
from aspose.slides import LoadOptions
from aspose.slides.export import (MarkdownSaveOptions, MarkdownExportType)

class TestConvert(TestCase):
    def setUp(self):
        if os.path.exists("index.md"):
            os.remove("index.md")
        if os.path.exists("Images"):
            shutil.rmtree("Images")
        if os.path.exists("output"):
            shutil.rmtree("output")

    def test_convert_simple(self):
        with open(self._test_file_path, "rb") as file_stream:
            converter = AsposeSlidesConverter()
            md_str = converter.convert(file_stream, None)
        self.assertTrue(md_str)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    def test_convert_text_only(self):
        with open(self._test_file_path, "rb") as file_stream:
            converter = AsposeSlidesConverter()
            save_options = MarkdownSaveOptions()
            save_options.export_type = MarkdownExportType.TEXT_ONLY
            md_str = converter.convert(file_stream, None, save_options = save_options)
        self.assertTrue(md_str)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    def test_convert_sequential(self):
        with open(self._test_file_path, "rb") as file_stream:
            converter = AsposeSlidesConverter()
            save_options = MarkdownSaveOptions()
            save_options.export_type = MarkdownExportType.SEQUENTIAL
            md_str = converter.convert(file_stream, None, save_options = save_options)
        self.assertTrue(md_str)
        self.assertTrue(os.path.exists("index.md"))
        self.assertTrue(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    def test_convert_custom_folders(self):
        with open(self._test_file_path, "rb") as file_stream:
            converter = AsposeSlidesConverter()
            save_options = MarkdownSaveOptions()
            save_options.export_type = MarkdownExportType.SEQUENTIAL
            save_options.base_path = "output"
            save_options.images_save_folder_name = "pics"
            md_str = converter.convert(file_stream, None, save_options = save_options)
        self.assertTrue(md_str)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertTrue(os.path.exists("output"))
        self.assertFalse(os.path.exists("output/Images"))
        self.assertTrue(os.path.exists("output/index.md"))
        self.assertTrue(os.path.exists("output/pics"))

    def test_convert_password(self):
        with open(self._test_password_file_path, "rb") as file_stream:
            converter = AsposeSlidesConverter()
            load_options = LoadOptions()
            load_options.password = "password"
            md_str = converter.convert(file_stream, None, load_options = load_options)
        self.assertTrue(md_str)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    _test_data_path = os.path.join(os.path.dirname(__file__), "test_data")
    _test_file_path = os.path.join(_test_data_path, "test.pptx")
    _test_password_file_path = os.path.join(_test_data_path, "test_password.pptx")
