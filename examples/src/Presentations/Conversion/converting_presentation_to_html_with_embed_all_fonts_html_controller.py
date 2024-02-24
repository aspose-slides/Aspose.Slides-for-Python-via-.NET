import aspose.slides as slides


def convert_to_html_with_embed_all_fonts(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # exclude default presentation fonts
        font_name_exclude_list = []

        embed_fonts_controller = slides.export.EmbedAllFontsHtmlController(font_name_exclude_list)

        html_options_embed = slides.export.HtmlOptions()
        html_options_embed.html_formatter = slides.export.HtmlFormatter.create_custom_formatter(embed_fonts_controller)

        pres.save(global_opts.out_dir + "convert_to_html_with_embed_all_fonts_out.html", slides.export.SaveFormat.HTML,
                  html_options_embed)
