import aspose.slides as slides


def get_fonts_slide_substitution(global_opts):
    with slides.Presentation(global_opts.data_dir + "PresFontsSubst.pptx") as pres:
        for font_subst in pres.fonts_manager.get_substitutions([1, 2]):
            print(font_subst.original_font_name, "->", font_subst.substituted_font_name)
