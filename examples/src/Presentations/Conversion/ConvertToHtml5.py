import aspose.pydrawing as drawing
import aspose.slides as slides

def convert_to_html5():
    # The path to the documents directory
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        # Export a presentation containing slides transitions, animations, and shapes animations to HTML5
        options = slides.export.Html5Options()
        options.animate_shapes = True
        options.animate_transitions = True

        # Save presentation
        pres.save(outDir + "convert_to_html5_out.html", slides.export.SaveFormat.HTML5, options)