import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def export_ink_example():
    with slides.Presentation(dataDir + "InkOptions.pptx") as pres:
        options = slides.export.PdfOptions()
        # Hide ink objects
        options.ink_options.hide_ink = True
        # Save result
        pres.save(outDir + "HideInkDemo.pdf", slides.export.SaveFormat.PDF, options)
        
        # Show Ink objects
        options.ink_options.hide_ink = False
        # Set using ROP operation for rendering brush
        options.ink_options.interpret_mask_op_as_opacity = False
        # Save result
        pres.save(outDir + "ROPInkDemo.pdf", slides.export.SaveFormat.PDF, options)
