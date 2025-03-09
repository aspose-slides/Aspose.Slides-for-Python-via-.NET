import aspose.slides as slides
import io


def image_quality_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "ImageQuality.pptx") as pres:
        img = pres.images[0].image

        # Saves the first image to the memory stream in JPEG format with quality 80.
        ms = io.BytesIO()
        img.save(ms, slides.ImageFormat.JPEG, 80)

        img.save(global_opts.out_dir + "ImageQuality-out.jpg", slides.ImageFormat.JPEG, 100)
