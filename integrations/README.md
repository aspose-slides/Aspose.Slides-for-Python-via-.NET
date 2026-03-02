# Integrations

This folder contains Aspose.Slides extensions for [MarkItDown](https://github.com/microsoft/markitdown), [Docling](https://github.com/docling-project/docling), and [Datalab Marker](https://github.com/VikParuchuri/marker).

Each extension is a bridge that wraps [Aspose.Slides for Python via .NET](https://products.aspose.com/slides/python-net) for a specific document-conversion framework, enabling PowerPoint-to-Markdown conversion.

Each extension is located in a subfolder and is installed separately. The extensions are not available on PyPI, so you should install them by cloning this repository and installing the project(s) you need from the corresponding local folder.

```bash
git clone https://github.com/aspose-slides/Aspose.Slides-for-Python-via-.NET.git
cd Aspose.Slides-for-Python-via-.NET/integrations
```

# Aspose Slides MarkItDown Plugin

This plugin allows converting PowerPoint presentations into Markdown format with Aspose.Slides using MarkItDown library.

## Installation

```bash
pip install ./markitdown-plugin
```

Once the plugin package is installed, verify that it is available to MarkItDown by running:

```bash
markitdown --list-plugins
```

## Command Line Usage

To use the plugin for presentation conversion use the `--use-plugins` flag like as follows:

```bash
markitdown --use-plugins presentation.pptx -o output.md
```

## Python Code Usage

This python code does the same as the command above:

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins = True)
result = md.convert(presentation.pptx)
with open("output.md", "w") as markdown_file:
    markdown_file.write(result.text_content)
```

## Using options

Use `save_options` parameter to specify save options. In the example below, the file & images are saved into a custom directory:

```python
from markitdown import MarkItDown
from aspose.slides.export import (MarkdownSaveOptions, MarkdownExportType)

save_options = MarkdownSaveOptions()
save_options.export_type = MarkdownExportType.SEQUENTIAL
save_options.base_path = "output"
save_options.images_save_folder_name = "pics"

md = MarkItDown(enable_plugins = True)
md.convert(presentation.pptx, save_options = save_options)
```

Use `load_options` parameter to specify load options. In the example below, a password-protected presentation is loaded:

```python
from markitdown import MarkItDown
from aspose.slides import LoadOptions

load_options = LoadOptions()
load_options.password = "presentation_password"

md = MarkItDown(enable_plugins = True)
md.convert(presentation.pptx, load_options = load_options)
```

# Aspose Slides Docling Backend

This extension allows converting PowerPoint presentations into Markdown format with Aspose.Slides using Docling library.

## Installation

```bash
pip install ./docling-backend
```

## Usage

```python
from pathlib import Path
from docling.datamodel.document import InputDocument
from docling.datamodel.base_models import InputFormat
from aspose_slides_docling_backend import AsposeSlidesBackend

input_doc = InputDocument(
    path_or_stream = Path("presentation.ppt"),
    format = InputFormat.PPTX,
    backend = AsposeSlidesBackend,
    filename = "presentation.ppt")

backend = AsposeSlidesBackend(input_doc, Path("presentation.ppt"))
document = backend.convert()
markdown_content = document.export_to_markdown()

with open("presentation.md", "w") as markdown_file:
    markdown_file.write(markdown_content)
```

## Using options

Use `save_options` parameter to specify save options. In the example below, the file & images are saved to a custom directory:

```python
from pathlib import Path
from docling.datamodel.document import InputDocument
from docling.datamodel.base_models import InputFormat
from aspose_slides_docling_backend import AsposeSlidesBackend
from aspose.slides.export import (MarkdownSaveOptions, MarkdownExportType)

input_doc = InputDocument(
    path_or_stream = Path("presentation.ppt"),
    format = InputFormat.PPTX,
    backend = AsposeSlidesBackend,
    filename = "presentation.ppt")

backend = AsposeSlidesBackend(input_doc, Path("presentation.ppt"))
document = backend.convert()


save_options = MarkdownSaveOptions()
save_options.export_type = MarkdownExportType.SEQUENTIAL
save_options.base_path = "output"
save_options.images_save_folder_name = "pics"
document.export_to_markdown(save_options = save_options)
```

Use `load_options` parameter to specify load options. In the example below, a password-protected presentation is loaded:

```python
from pathlib import Path
from docling.datamodel.document import InputDocument
from docling.datamodel.base_models import InputFormat
from aspose_slides_docling_backend import AsposeSlidesBackend
from aspose.slides import LoadOptions

input_doc = InputDocument(
    path_or_stream = Path("presentation.ppt"),
    format = InputFormat.PPTX,
    backend = AsposeSlidesBackend,
    filename = "presentation.ppt")

backend = AsposeSlidesBackend(input_doc, Path("presentation.ppt"))

load_options = LoadOptions()
load_options.password = "presentation_password"
document = backend.convert(load_options = load_options)
document.export_to_markdown()
```

# Aspose Slides Datalab Marker Extension

This extension allows converting PowerPoint presentations into Markdown format with Aspose.Slides using Datalab Marker library.

## Installation

```bash
pip install ./marker-extension
```

## Command Line Usage

To use the extension to convert a file into md set the `--converter_cls` option value like as follows:

```bash
marker_single presentation.pptx --converter_cls=aspose_slides_marker_extension.AsposeSlidesConverter --output_dir out_md
```

## Python Code Usage

To convert a presentation into markdown format, use python code like as follows:

```python
from marker.output import text_from_rendered
from aspose_slides_marker_extension import AsposeSlidesConverter

converter = AsposeSlidesConverter()
rendered = converter("presentation.pptx")
markdown_content, _, images = text_from_rendered(rendered)
with open("presentation.md", "w") as markdown_file:
    markdown_file.write(markdown_content)
```

## Using options

Use `save_options` parameter to specify save options. In the example below, the file & images are saved to a custom directory:

```python
from marker.output import text_from_rendered
from aspose_slides_marker_extension import AsposeSlidesConverter
from aspose.slides.export import MarkdownSaveOptions, MarkdownExportType

converter = AsposeSlidesConverter()

save_options = MarkdownSaveOptions()
save_options.export_type = MarkdownExportType.SEQUENTIAL
save_options.base_path = "output"
save_options.images_save_folder_name = "pics"

rendered = converter("presentation.pptx", save_options = save_options)
markdown_content, _, images = text_from_rendered(rendered)
with open("presentation.md", "w") as markdown_file:
    markdown_file.write(markdown_content)
```

Use `load_options` parameter to specify load options. In the example below, a password-protected presentation is loaded:

```python
from marker.output import text_from_rendered
from aspose_slides_marker_extension import AsposeSlidesConverter
from aspose.slides import LoadOptions

converter = AsposeSlidesConverter()

load_options = LoadOptions()
load_options.password = "presentation_password"

rendered = converter("presentation.pptx", load_options = load_options)
markdown_content, _, images = text_from_rendered(rendered)
with open("presentation.md", "w") as markdown_file:
    markdown_file.write(markdown_content)
```
