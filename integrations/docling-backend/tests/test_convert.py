import os
import shutil

from io import BytesIO
from pathlib import Path
from unittest import TestCase
from aspose_slides_docling_backend import AsposeSlidesBackend
from aspose.slides import LoadOptions
from aspose.slides.export import (MarkdownSaveOptions, MarkdownExportType)
from docling.datamodel.document import InputDocument
from docling.datamodel.base_models import InputFormat

class TestConvert(TestCase):
    def setUp(self):
        if os.path.exists("index.md"):
            os.remove("index.md")
        if os.path.exists("Images"):
            shutil.rmtree("Images")
        if os.path.exists("output"):
            shutil.rmtree("output")

    def test_convert_simple(self):
        input_doc = InputDocument(
            path_or_stream = Path(self._test_file_path),
            format = InputFormat.PPTX,
            backend = AsposeSlidesBackend,
            filename = "test.ppt")
        backend = AsposeSlidesBackend(input_doc, Path(self._test_file_path))
        document = backend.convert()
        markdown_content = document.export_to_markdown()
        self.assertTrue(markdown_content)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    def test_convert_simple_stream(self):
        with open(self._test_file_path, "rb") as file_reader:
            file_stream = BytesIO(file_reader.read())
            input_doc = InputDocument(
                path_or_stream = file_stream,
                format = InputFormat.PPTX,
                backend = AsposeSlidesBackend,
                filename = "test.ppt")
            backend = AsposeSlidesBackend(input_doc, file_stream)
            document = backend.convert()
            markdown_content = document.export_to_markdown()
            self.assertTrue(markdown_content)
            self.assertFalse(os.path.exists("index.md"))
            self.assertFalse(os.path.exists("Images"))
            self.assertFalse(os.path.exists("output"))

    def test_convert_text_only(self):
        input_doc = InputDocument(
            path_or_stream = Path(self._test_file_path),
            format = InputFormat.PPTX,
            backend = AsposeSlidesBackend,
            filename = "test.ppt")
        backend = AsposeSlidesBackend(input_doc, Path(self._test_file_path))
        document = backend.convert()
        save_options = MarkdownSaveOptions()
        save_options.export_type = MarkdownExportType.TEXT_ONLY
        markdown_content = document.export_to_markdown(save_options = save_options)
        self.assertTrue(markdown_content)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    def test_convert_sequential(self):
        input_doc = InputDocument(
            path_or_stream = Path(self._test_file_path),
            format = InputFormat.PPTX,
            backend = AsposeSlidesBackend,
            filename = "test.ppt")
        backend = AsposeSlidesBackend(input_doc, Path(self._test_file_path))
        document = backend.convert()
        save_options = MarkdownSaveOptions()
        save_options.export_type = MarkdownExportType.SEQUENTIAL
        markdown_content = document.export_to_markdown(save_options = save_options)
        self.assertTrue(markdown_content)
        self.assertTrue(os.path.exists("index.md"))
        self.assertTrue(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    def test_convert_custom_folders(self):
        input_doc = InputDocument(
            path_or_stream = Path(self._test_file_path),
            format = InputFormat.PPTX,
            backend = AsposeSlidesBackend,
            filename = "test.ppt")
        backend = AsposeSlidesBackend(input_doc, Path(self._test_file_path))
        document = backend.convert()
        save_options = MarkdownSaveOptions()
        save_options.export_type = MarkdownExportType.SEQUENTIAL
        save_options.base_path = "output"
        save_options.images_save_folder_name = "pics"
        markdown_content = document.export_to_markdown(save_options = save_options)
        self.assertTrue(markdown_content)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertTrue(os.path.exists("output"))
        self.assertFalse(os.path.exists("output/Images"))
        self.assertTrue(os.path.exists("output/index.md"))
        self.assertTrue(os.path.exists("output/pics"))

    def test_convert_password(self):
        input_doc = InputDocument(
            path_or_stream = Path(self._test_password_file_path),
            format = InputFormat.PPTX,
            backend = AsposeSlidesBackend,
            filename = "test.ppt")
        backend = AsposeSlidesBackend(input_doc, Path(self._test_password_file_path))
        load_options = LoadOptions()
        load_options.password = "password"
        document = backend.convert(load_options = load_options)
        markdown_content = document.export_to_markdown()
        self.assertTrue(markdown_content)
        self.assertFalse(os.path.exists("index.md"))
        self.assertFalse(os.path.exists("Images"))
        self.assertFalse(os.path.exists("output"))

    _test_data_path = os.path.join(os.path.dirname(__file__), "test_data")
    _test_file_path = os.path.join(_test_data_path, "test.pptx")
    _test_password_file_path = os.path.join(_test_data_path, "test_password.pptx")
