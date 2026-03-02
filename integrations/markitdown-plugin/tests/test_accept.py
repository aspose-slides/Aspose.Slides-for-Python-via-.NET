from unittest import TestCase
from markitdown import StreamInfo
from aspose_slides_markitdown_plugin import AsposeSlidesConverter

class TestAccept(TestCase):

    def test_accept_mime_type(self):
        converter = AsposeSlidesConverter()
        stream_info = StreamInfo(mimetype = "application/vnd.ms-powerpoint.suffix")
        accepts = converter.accepts(None, stream_info)
        self.assertTrue(accepts)

    def test_accept_extension(self):
        converter = AsposeSlidesConverter()
        stream_info = StreamInfo(extension = ".ppt")
        accepts = converter.accepts(None, stream_info)
        self.assertTrue(accepts)

    def test_accept_invalid(self):
        converter = AsposeSlidesConverter()
        stream_info = StreamInfo(extension = ".pptf", mimetype="text/json")
        accepts = converter.accepts(None, stream_info)
        self.assertFalse(accepts)
