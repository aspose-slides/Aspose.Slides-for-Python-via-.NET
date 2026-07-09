import aspose.slides as slides


def html5_pictures_compression_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "PresentationPic.pptx") as pres:
        # Set image compression level
        options = slides.export.Html5Options()
        options.pictures_compression = slides.export.PicturesCompression.DPI150

        # Save result
        pres.save(global_opts.out_dir + "PresentationPic150.html", slides.export.SaveFormat.HTML5, options)
