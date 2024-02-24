import aspose.slides as slides


def remove_vba_macros(global_opts):
    # Instantiate Presentation
    with slides.Presentation(global_opts.data_dir + "VBA.pptm") as presentation:
        # Access the Vba module and remove
        presentation.vba_project.modules.remove(presentation.vba_project.modules[0])

        # Save Presentation
        presentation.save(global_opts.out_dir + "vba_RemovedVBAMacros_out.pptm", slides.export.SaveFormat.PPTM)
