import aspose.slides as slides


def manage_presentation_normal_view_state(global_opts):
    with slides.Presentation() as pres:
        pres.view_properties.normal_view_properties.horizontal_bar_state = slides.SplitterBarStateType.RESTORED
        pres.view_properties.normal_view_properties.vertical_bar_state = slides.SplitterBarStateType.MAXIMIZED

        pres.view_properties.normal_view_properties.restored_top.auto_adjust = True
        pres.view_properties.normal_view_properties.restored_top.dimension_size = 80
        pres.view_properties.normal_view_properties.show_outline_icons = True

        pres.save(global_opts.out_dir + "presentation_normal_view_state.pptx", slides.export.SaveFormat.PPTX)
