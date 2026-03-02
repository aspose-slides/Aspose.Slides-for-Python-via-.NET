import os

from io import BytesIO, TextIOWrapper
from docling_core.types.doc import DoclingDocument
from aspose.slides import Presentation
from aspose.slides.export import SaveFormat, MarkdownSaveOptions, MarkdownExportType

class AsposeSlidesDoclingDocument(DoclingDocument):
    def __init__(self, aspose_slides_presentation: Presentation):
        self._aspose_slides_presentation = aspose_slides_presentation

    def export_to_markdown(self, **kwargs) -> str:
        if self._aspose_slides_presentation:
            save_options = kwargs.get("save_options")
            if save_options and save_options.export_type != MarkdownExportType.TEXT_ONLY:
                return self._convert_with_files(save_options)
            else:
                return self._convert_text_only(save_options)
        else:
            return super().export_to_markdown(**kwargs)

    def _convert_with_files(self, save_options: MarkdownSaveOptions) -> str:
        index_file_path = "index.md"
        if save_options and save_options.base_path:
            os.makedirs(save_options.base_path, exist_ok = True)
            index_file_path = os.path.join(save_options.base_path, index_file_path)
        if save_options:
            self._aspose_slides_presentation.save(index_file_path, SaveFormat.MD, save_options)
        else:
            self._aspose_slides_presentation.save(index_file_path, SaveFormat.MD)
        with open(index_file_path, "r") as index_file:
            md_str = index_file.read()
            return md_str

    def _convert_text_only(self, save_options: MarkdownSaveOptions) -> str:
        md_stream = BytesIO()
        if save_options:
            self._aspose_slides_presentation.save(md_stream, SaveFormat.MD, save_options)
        else:
            self._aspose_slides_presentation.save(md_stream, SaveFormat.MD)
        md_stream.seek(0)
        md_text = TextIOWrapper(md_stream)
        md_str = md_text.read()
        return md_str
