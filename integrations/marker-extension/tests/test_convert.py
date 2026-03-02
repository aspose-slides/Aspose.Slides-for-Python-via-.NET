import os
import shutil

from io import BytesIO
from pathlib import Path
from unittest import TestCase
from marker.output import text_from_rendered
from aspose.slides import LoadOptions
from aspose.slides.export import MarkdownSaveOptions, MarkdownExportType
from aspose_slides_marker_extension import AsposeSlidesConverter

class TestConvert(TestCase):
    def setUp(self):
        if os.path.exists("index.md"):
            os.remove("index.md")
        if os.path.exists("Images"):
            shutil.rmtree("Images")
        if os.path.exists("output"):
            shutil.rmtree("output")

    def test_convert_simple(self):
        converter = AsposeSlidesConverter()
        rendered = converter(self._test_file_path)
        markdown_content, _, _ = text_from_rendered(rendered)
        self.assertTrue(markdown_content)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    def test_convert_simple_stream(self):
        with open(self._test_file_path, "rb") as file_reader:
            file_stream = BytesIO(file_reader.read())
            converter = AsposeSlidesConverter()
            rendered = converter(file_stream)
            markdown_content, _, _ = text_from_rendered(rendered)
            self.assertTrue(markdown_content)
            self.assertFalse(os.path.exists("index.md"))
            self.assertFalse(os.path.exists("Images"))
            self.assertFalse(os.path.exists("output"))

    def test_convert_text_only(self):
        converter = AsposeSlidesConverter()
        save_options = MarkdownSaveOptions()
        save_options.export_type = MarkdownExportType.TEXT_ONLY
        rendered = converter(self._test_file_path, save_options = save_options)
        markdown_content, _, _ = text_from_rendered(rendered)
        self.assertTrue(markdown_content)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    def test_convert_sequential(self):
        converter = AsposeSlidesConverter()
        save_options = MarkdownSaveOptions()
        save_options.export_type = MarkdownExportType.SEQUENTIAL
        rendered = converter(self._test_file_path, save_options = save_options)
        markdown_content, _, _ = text_from_rendered(rendered)
        self.assertTrue(markdown_content)
        self.assertTrue(os.path.exists("index.md"))
        self.assertTrue(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    def test_convert_custom_folders(self):
        converter = AsposeSlidesConverter()
        save_options = MarkdownSaveOptions()
        save_options.export_type = MarkdownExportType.SEQUENTIAL
        save_options.base_path = "output"
        save_options.images_save_folder_name = "pics"
        rendered = converter(self._test_file_path, save_options = save_options)
        markdown_content, _, _ = text_from_rendered(rendered)
        self.assertTrue(markdown_content)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertTrue(os.path.exists("output"))
        self.assertFalse(os.path.exists("output/Images"))
        self.assertTrue(os.path.exists("output/index.md"))
        self.assertTrue(os.path.exists("output/pics"))

    def test_convert_password(self):
        converter = AsposeSlidesConverter()
        load_options = LoadOptions()
        load_options.password = "password"
        rendered = converter(self._test_password_file_path, load_options = load_options)
        markdown_content, _, _ = text_from_rendered(rendered)
        self.assertTrue(markdown_content)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    _test_data_path = os.path.join(os.path.dirname(__file__), "test_data")
    _test_file_path = os.path.join(_test_data_path, "test.pptx")
    _test_password_file_path = os.path.join(_test_data_path, "test_password.pptx")
