import aspose.slides as slides
import os

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def convert_html_embedding_images():
    # Path to source presentation
    presentation_name = dataDir + "PresentationDemo.pptx"
    # Path to HTML document
    out_file_path = outDir + "HTMLConvertion"
    
    with slides.Presentation(presentation_name) as pres:
        options = slides.export.Html5Options()
        
        # Force do not save images in HTML5 document
        options.embed_images = False
        # Set path for external images
        options.output_path = outDir
        
        # Create directory for output HTML document
        if not os.access(out_file_path, os.F_OK):
            os.makedirs(out_file_path, exist_ok=True)
        
        # Save presentation in HTML5 format.
        pres.save(out_file_path + "/pres.html", slides.export.SaveFormat.HTML5, options)
