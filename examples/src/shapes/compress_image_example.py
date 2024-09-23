import aspose.slides as slides
import os


def compress_image_example(global_opts):
    # Path to source presentation
    presentation_name = global_opts.data_dir + "CroppedImage.pptx"
    # Path to output document
    out_file_path = global_opts.out_dir + "CroppedImage-Compress-out.pptx"

    with slides.Presentation(presentation_name) as pres:
        slide = pres.slides[0]

        # Get the PictureFrame from the slide
        pic_frame = slide.shapes[0]

        # Compress the image with a target resolution of 150 DPI (Web resolution) and remove cropped areas
        result = pic_frame.picture_format.compress_image(True, 150)

        # Check the result of the compression
        if result:
            print("Image successfully compressed.")
        else:
            print("Image compression failed or no changes were necessary.")

        # Save result
        pres.save(out_file_path, slides.export.SaveFormat.PPTX)

        # Check size
        print("Source presentation length\t =", os.stat(presentation_name).st_size)
        print("Resulting presentation length\t =", os.stat(out_file_path).st_size)
