from io import BytesIO
from pathlib import Path
from typing import Union
from typing_extensions import override
from docling_core.types.doc import DoclingDocument
from docling.backend.abstract_backend import (DeclarativeDocumentBackend, PaginatedDocumentBackend)
from docling.datamodel.base_models import InputFormat
from aspose.slides import (Presentation, LoadOptions)
from .aspose_slides_docling_document import AsposeSlidesDoclingDocument

class AsposeSlidesBackend(DeclarativeDocumentBackend, PaginatedDocumentBackend):
    def __init__(self, in_doc: "InputDocument", path_or_stream: Union[BytesIO, Path]):
        super().__init__(in_doc, path_or_stream)
        self._aspose_slides_presentation = None
        self._path_or_stream = path_or_stream

    def convert(self, **kwargs) -> DoclingDocument:
        self._init_aspose_slides_presentation(self._path_or_stream, kwargs.get("load_options"))
        return AsposeSlidesDoclingDocument(self._aspose_slides_presentation)

    @override
    def is_valid(self) -> bool:
        return self._aspose_slides_presentation != None

    @override
    def page_count(self) -> int:
        return len(self._aspose_slides_presentation.slides)

    @classmethod
    @override
    def supports_pagination(cls) -> bool:
        return True

    @classmethod
    @override
    def supported_formats(cls) -> set[InputFormat]:
        return {InputFormat.PPTX}

    def _init_aspose_slides_presentation(self, path_or_stream: Union[BytesIO, Path], load_options: LoadOptions):
        if isinstance(path_or_stream, Path):
            if load_options:
                self._aspose_slides_presentation = Presentation(str(path_or_stream), load_options)
            else:
                self._aspose_slides_presentation = Presentation(str(path_or_stream))
        elif isinstance(path_or_stream, BytesIO):
            if load_options:
                self._aspose_slides_presentation = Presentation(path_or_stream, load_options)
            else:
                self._aspose_slides_presentation = Presentation(path_or_stream)