import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def specify_default_text_language():
    load_options = slides.LoadOptions()
    load_options.default_text_language = "en-US"
    with slides.Presentation(load_options) as pres:
        # Add new rectangle shape with text
        shp = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 50, 150, 50)
        shp.text_frame.text = "New Text"
        
        # Check the first portion language
        print(shp.text_frame.paragraphs[0].portions[0].portion_format.language_id)
