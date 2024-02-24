import aspose.slides as slides
import os


def convert_html_embedding_images(global_opts):
    content_dir = global_opts.out_dir + "HTMLConversion/"
    with slides.Presentation(global_opts.data_dir + "PresentationDemo.pptx") as pres:
        html5_options = slides.export.Html5Options()
        
        # Force do not save images in HTML5 document
        html5_options.embed_images = False
        # Set path for external images
        html5_options.output_path = global_opts.out_dir
        
        # Create directory for output HTML document
        try:
            os.rmdir(content_dir)
        except OSError:
            pass

        os.makedirs(content_dir, exist_ok=True)
        
        # Save presentation in HTML5 format.
        pres.save(content_dir + "pres.html", slides.export.SaveFormat.HTML5, html5_options)
