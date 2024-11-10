import aspose.slides as slides


def grid_properties(global_opts):
    with slides.Presentation() as pres:
        # Set grid spacing
        pres.view_properties.grid_spacing = 72

        # Save presentation
        pres.save(global_opts.out_dir + "GridProperties-out.pptx", slides.export.SaveFormat.PPTX)
