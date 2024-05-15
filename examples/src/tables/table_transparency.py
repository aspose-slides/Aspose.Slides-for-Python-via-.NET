import aspose.slides as slides


def table_transparency(global_opts):
    # The path to the presentation
    with slides.Presentation(global_opts.data_dir + "TableTransparency.pptx") as pres:
        table = pres.slides[0].shapes[1]
        table.table_format.transparency = 0.62
        pres.save(global_opts.out_dir + "TableTransparency_out.pptx", slides.export.SaveFormat.PPTX)
