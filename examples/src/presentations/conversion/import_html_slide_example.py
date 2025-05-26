import aspose.slides as slides


def import_html_slide_example(global_opts):
    with slides.Presentation() as pres, open(global_opts.data_dir + "TestHtml.html", "rb") as input_stream:
        pres.slides.insert_from_html(0, input_stream, True)
        pres.save(global_opts.out_dir + "OutputConvertedHtml.pptx", slides.export.SaveFormat.PPTX)
