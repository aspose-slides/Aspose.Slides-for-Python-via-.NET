import aspose.slides as slides


def convert_to_xml(global_opts):
    with slides.Presentation() as presentation:
        presentation.save(global_opts.out_dir + "example.xml", slides.export.SaveFormat.XML)
