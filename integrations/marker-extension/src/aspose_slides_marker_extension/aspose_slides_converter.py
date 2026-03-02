import os

from typing import Any, Dict, List, Optional
from io import BytesIO, TextIOWrapper
from marker.converters.pdf import PdfConverter
from marker.renderers.markdown import MarkdownOutput
from aspose.slides import Presentation, LoadOptions
from aspose.slides.export import SaveFormat, MarkdownSaveOptions, MarkdownExportType

class AsposeSlidesConverter:
    def __init__(
        self,
        artifact_dict: Dict[str, Any] = None,
        processor_list: Optional[List[str]] = None,
        renderer: str | None = None,
        llm_service: str | None = None,
        config = None):

        self._base_converter = PdfConverter(
            config = config,
            artifact_dict = artifact_dict,
            processor_list = processor_list,
            renderer = renderer,
            llm_service = llm_service)

    def __call__(self, filepath: str | BytesIO, load_options: LoadOptions = None, save_options: MarkdownSaveOptions = None):
        try:
            with self._load_presentation(filepath, load_options) as presentation:
                if save_options and save_options.export_type != MarkdownExportType.TEXT_ONLY:
                    return self._convert_with_files(presentation, save_options)
                else:
                    return self._convert_text_only(presentation, save_options)
        except:
            return self._base_converter(filepath)

    def _load_presentation(self, file_stream: str | BytesIO, load_options: LoadOptions) -> Presentation:
        if load_options:
            return Presentation(file_stream, load_options)
        else:
            return Presentation(file_stream)

    def _convert_with_files(self, presentation: Presentation, save_options: MarkdownSaveOptions) -> MarkdownOutput:
        index_file_path = "index.md"
        if save_options and save_options.base_path:
            os.makedirs(save_options.base_path, exist_ok = True)
            index_file_path = os.path.join(save_options.base_path, index_file_path)
        if save_options:
            presentation.save(index_file_path, SaveFormat.MD, save_options)
        else:
            presentation.save(index_file_path, SaveFormat.MD)
        with open(index_file_path, "r") as index_file:
            md_str = index_file.read()
            return MarkdownOutput(markdown = md_str, images = {}, metadata = {})

    def _convert_text_only(self, presentation: Presentation, save_options: MarkdownSaveOptions) -> MarkdownOutput:
        md_stream = BytesIO()
        if save_options:
            presentation.save(md_stream, SaveFormat.MD, save_options)
        else:
            presentation.save(md_stream, SaveFormat.MD)
        md_stream.seek(0)
        md_text = TextIOWrapper(md_stream)
        md_str = md_text.read()
        return MarkdownOutput(markdown = md_str, images = {}, metadata = {})
