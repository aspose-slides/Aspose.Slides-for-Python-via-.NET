import aspose.slides as slides
import os

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def delete_picture_cropped_areas_example():
    # Path to source presentation
    presentation_name = dataDir + "CroppedImage.pptx"
    # Path to output document
    out_file_path = outDir + "CroppedImage-out.pptx"
    
    with slides.Presentation(presentation_name) as pres:
        # Gets the first slide
        slide = pres.slides[0]
        
        # Gets the PictureFrame
        pic_frame = slide.shapes[0]
        
        # Deletes cropped areas of the PictureFrame image
        cropped_image = pic_frame.picture_format.delete_picture_cropped_areas()
        
        # Save result
        pres.save(out_file_path, slides.export.SaveFormat.PPTX)
        
        # Check size
        print("Source presentation length\t =", os.stat(presentation_name).st_size)
        print("Resulting presentation length\t =", os.stat(out_file_path).st_size)
