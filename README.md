# Python PowerPoint API. Python PPTX, PPT

[Aspose.Slides for Python via .NET](https://products.aspose.com/slides/python-net) is a powerful class library for processing and manipulating presentations. Using this product, applications or developers get to view or read, edit, print, and convert Microsoft PowerPoint presentations (PPT, PPTX) and presentations in other formats (ODP) without third-party applications or dependencies.

<p align="center">
  <a title="Download complete Aspose.Slides for Python via .NET source code" href="https://github.com/aspose-slides/Aspose.Slides-for-Python-via-.NET/archive/master.zip">
	<img src="https://raw.github.com/AsposeExamples/java-examples-dashboard/master/images/downloadZip-Button-Large.png" />
  </a>
</p>

## **Python PowerPoint API Features**

Aspose.Slides for Python allows you to

* Create or generate presentations.
* Load and view presentations.
* Convert presentations to PDF, Word, images (JPG, PNG), and other [supported formats](https://docs.aspose.com/slides/python-net/supported-file-formats/).
* Access, edit, and manipulate a slide's contents (texts, shapes, etc.).

To view a comprehensive list of features, see the **Aspose.Slides for Python via .NET** [**Features page**](https://docs.aspose.com/slides/python-net/features-overview/).

## **Read & Modify Presentations**

**Microsoft PowerPoint:** PPT, PPTX, PPS, POT, PPSX, PPTM, PPSM, POTX, POTM\
**OpenOffice:** ODP, OTP

## **Save Presentations As**

**Fixed Layout:** PDF, PDF/A, XPS
**Image:** JPEG, PNG, BMP, TIFF, GIF, SVG
**Web:** HTML

## **Supported Environments**

Aspose.Slides for Python via .NET can be used on any 64-bit or 32-bit operating system where Python 3.5 or later is installed.

**Microsoft Windows:** Windows XP (x64, x86) and later; Windows 2003 Server (x64, x86) and later.

**Linux**: Ubuntu; OpenSUSE; CentOS; and others.

## **Get Started with Aspose.Slides for Python**

`pip` provides the easiest path to downloading and installing [Aspose.Slides for Python via .NET](https://pypi.org/project/aspose.slides/).

To install Aspose.Slides, run this command: `pip install aspose.slides`

## **Create a Presentation from Scratch**

```python
import aspose.slides as slides

# Instantiates a Presentation object that represents a presentation file
with slides.Presentation() as presentation:
    slide = presentation.slides[0]
    # Adds an autoshape with type set to line
    slide.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)
    presentation.save("NewPresentation_out.pptx", slides.export.SaveFormat.PPTX)
```

## **Convert a Presentation to PDF**

```python
import aspose.slides as slides

# Instantiates a Presentation object that represents a presentation file
presentation = slides.Presentation("PowerPoint.pptx")

# Saves the presentation to PDF
presentation.save("PPTX-to-PDF.pdf", slides.export.SaveFormat.PDF)
```

[Home](https://www.aspose.com/) | [Product Page](https://products.aspose.com/slides/python-net) | [Docs](https://docs.aspose.com/slides/python-net/) | [Demos](https://products.aspose.app/slides/family) | [API Reference](https://docs.aspose.com/slides/python-net/api-reference/) | [Examples](https://github.com/aspose-slides/Aspose.Slides-for-Python-via-.NET/) | [Blog](https://blog.aspose.com/category/slides/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/slides) | [Temporary License](https://purchase.aspose.com/temporary-license)
