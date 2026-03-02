import os
from io import (BytesIO, TextIOWrapper)
from typing import BinaryIO, Any
from aspose.slides import (Presentation, LoadOptions)
from aspose.slides.export import (SaveFormat, MarkdownSaveOptions, MarkdownExportType)
from markitdown import (MarkItDown, DocumentConverter, DocumentConverterResult, StreamInfo)

def register_converters(markitdown: MarkItDown, **kwargs):
    markitdown.register_converter(AsposeSlidesConverter())

class AsposeSlidesConverter(DocumentConverter):
    def accepts(self, file_stream: BinaryIO, stream_info: StreamInfo, **kwargs: Any) -> bool:
        if stream_info.mimetype:
            mime_type = stream_info.mimetype.lower()
            for mime_prefix in self._good_mime_type_prefixes:
                if mime_type.startswith(mime_prefix):
                    return True
        if stream_info.extension and stream_info.extension.lower() in self._good_extensions:
            return True
        return False

    def convert(self, file_stream: BinaryIO, stream_info: StreamInfo, **kwargs: Any) -> DocumentConverterResult:
        with self._load_presentation(file_stream, kwargs.get("load_options")) as presentation:
            save_options = kwargs.get("save_options")
            if save_options and save_options.export_type != MarkdownExportType.TEXT_ONLY:
                return self._convert_with_files(presentation, save_options)
            else:
                return self._convert_text_only(presentation, save_options)

    def _load_presentation(self, file_stream: BinaryIO, load_options: LoadOptions) -> Presentation:
        if load_options:
            return Presentation(file_stream, load_options)
        else:
            return Presentation(file_stream)

    def _convert_with_files(self, presentation: Presentation, save_options: MarkdownSaveOptions) -> DocumentConverterResult:
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
            return DocumentConverterResult(title = None, markdown = md_str)

    def _convert_text_only(self, presentation: Presentation, save_options: MarkdownSaveOptions) -> DocumentConverterResult:
        md_stream = BytesIO()
        if save_options:
            presentation.save(md_stream, SaveFormat.MD, save_options)
        else:
            presentation.save(md_stream, SaveFormat.MD)
        md_stream.seek(0)
        md_text = TextIOWrapper(md_stream)
        md_str = md_text.read()
        return DocumentConverterResult(title = None, markdown = md_str)

    _good_mime_type_prefixes = [
        "application/vnd.openxmlformats-officedocument.presentationml",
        "application/vnd.ms-powerpoint",
        "application/vnd.oasis.opendocument.presentation"
    ]

    _good_extensions = [ ".pptx", ".ppsx", ".potx", ".ppt", ".pps", ".pot", ".pptm", ".ppsm", ".potm", ".odp", ".fodp", ".otp" ]

__plugin_interface_version__ = (1)
