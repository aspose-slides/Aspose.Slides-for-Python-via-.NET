import aspose.slides as slides

def convert_to_xps_with_options():
    #ExStart:ConvertWithXpsOptions
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        # Instantiate the TiffOptions class
        opts = slides.export.XpsOptions()

        # Save MetaFiles as PNG
        opts.save_metafiles_as_png = True

        # Save the presentation to XPS document
        pres.save(outDir + "convert_to_xps_with_options_out.xps", slides.export.SaveFormat.XPS, opts)
    #ExEnd:ConvertWithXpsOptions