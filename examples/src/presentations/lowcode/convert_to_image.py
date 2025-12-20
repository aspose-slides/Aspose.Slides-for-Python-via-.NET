import aspose.slides as slides


def convert_to_image(global_opts):
    with slides.Presentation(global_opts.data_dir + "ConvertExample.pptx") as pres:
        slides.lowcode.Convert.to_jpeg(pres, global_opts.out_dir + "ConvertedToJpeg.jpg")
        slides.lowcode.Convert.to_png(pres, global_opts.out_dir + "ConvertedToPng.png")
        slides.lowcode.Convert.to_tiff(pres, global_opts.out_dir + "ConvertedToTiff.tiff")
