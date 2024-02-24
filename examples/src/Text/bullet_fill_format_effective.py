import aspose.slides as slides


def bullet_fill_format_effective(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_bullet_data.pptx") as pres:
        auto_shape = pres.slides[0].shapes[0]
        for para in auto_shape.text_frame.paragraphs:
            bullet_format_effective = para.paragraph_format.bullet.get_effective()
            print("Bullet type: " + str(bullet_format_effective.type))
            if bullet_format_effective.type != slides.BulletType.NONE:
                print("Bullet fill type: " + str(bullet_format_effective.fill_format.fill_type))
                if bullet_format_effective.fill_format.fill_type == slides.FillType.SOLID:
                    print("Solid fill color: " + str(bullet_format_effective.fill_format.solid_fill_color))
                elif bullet_format_effective.fill_format.fill_type == slides.FillType.GRADIENT:
                    print("Gradient stops count: " + str(
                        len(bullet_format_effective.fill_format.gradient_format.gradient_stops)))
                    for gradStop in bullet_format_effective.fill_format.gradient_format.gradient_stops:
                        print(str(gradStop.position) + ": " + str(gradStop.color))
                elif bullet_format_effective.fill_format.fill_type == slides.FillType.PATTERN:
                    print("Pattern style: " + str(bullet_format_effective.fill_format.pattern_format.pattern_style))
                    print("Fore color: " + str(bullet_format_effective.fill_format.pattern_format.fore_color))
                    print("Back color: " + str(bullet_format_effective.fill_format.pattern_format.back_color))
