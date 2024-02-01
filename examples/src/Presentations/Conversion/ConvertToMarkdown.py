import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def convert_to_markdown():
    # Path to source presentation
    presentation_name = dataDir + "PresentationDemo.pptx"
    
    with slides.Presentation(presentation_name) as pres:
        # Create Markdown creation options
        md_options = slides.export.MarkdownSaveOptions()
        # Set parameter for render all items (items that are grouped will be rendered together).
        md_options.export_type = slides.export.MarkdownExportType.VISUAL
        # Set folder name for saving images
        md_options.images_save_folder_name = "md-images"
        # Set path for folder images
        md_options.base_path = outDir
        
        # Save presentation in Markdown format
        pres.save(outDir + "pres.md", slides.export.SaveFormat.MD, md_options)
