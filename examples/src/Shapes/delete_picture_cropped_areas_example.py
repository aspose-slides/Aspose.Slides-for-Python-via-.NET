import aspose.slides as slides
import os


def delete_picture_cropped_areas_example(global_opts):
    # Path to source presentation
    presentation_name = global_opts.data_dir + "CroppedImage.pptx"
    # Path to output document
    out_file_path = global_opts.out_dir + "CroppedImage-out.pptx"
    
    with slides.Presentation(global_opts.data_dir + "CroppedImage.pptx") as pres:
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
