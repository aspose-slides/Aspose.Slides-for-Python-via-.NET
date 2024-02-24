import aspose.slides as slides


def extracting_vba_macros(global_opts):
    with slides.Presentation(global_opts.data_dir + "VBA.pptm") as pres:
        # check if Presentation contains VBA Project
        if pres.vba_project is not None:
            for module in pres.vba_project.modules:
                print(module.name)
                print(module.source_code)
