import aspose.slides as slides


def java_script_link_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "JavaScriptLink.pptx") as pres:
        options = slides.export.PptxOptions()
        options.skip_java_script_links = True
        pres.save(global_opts.out_dir + "JavaScriptLink-out.pptx", slides.export.SaveFormat.PPTX, options)
