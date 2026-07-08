import io

import skia

import aspose.slides as slides

WINDOW = skia.ColorWHITE
WINDOW_TEXT = skia.ColorBLACK
CONTROL = skia.ColorSetRGB(240, 240, 240)
CONTROL_DARK = skia.ColorSetRGB(160, 160, 160)
CONTROL_DARK_DARK = skia.ColorSetRGB(105, 105, 105)
CONTROL_LIGHT = skia.ColorSetRGB(227, 227, 227)
CONTROL_LIGHT_LIGHT = skia.ColorWHITE


def _make_font(size=14):
    typeface = skia.Typeface("Arial") or skia.Typeface()
    return skia.Font(typeface, size)


def _draw_bevel(canvas, width, height, outer_color, mid_color, inner_color, innermost_color):
    """
    Draws a 4-line 3D bevel border using nested polylines per side
    """
    def polyline(points, color):
        paint = skia.Paint(Color=color, Style=skia.Paint.kStroke_Style, StrokeWidth=1)
        path = skia.Path()
        path.moveTo(*points[0])
        for p in points[1:]:
            path.lineTo(*p)
        canvas.drawPath(path, paint)

    polyline([(0, height - 1), (0, 0), (width - 1, 0)], outer_color)
    polyline([(1, height - 2), (1, 1), (width - 2, 1)], mid_color)
    polyline([(1, height - 1), (width - 1, height - 1), (width - 1, 1)], inner_color)
    polyline([(0, height), (width, height), (width, 0)], innermost_color)


def _surface_to_png_bytes(surface):
    image = surface.makeImageSnapshot()
    data = image.encodeToData(skia.kPNG, 100)
    buf = io.BytesIO(bytes(data))
    buf.seek(0)
    return buf


def _render_textbox_image(width, height, text):
    surface = skia.Surface(width, height)
    canvas = surface.getCanvas()
    canvas.clear(WINDOW)

    font = _make_font(14)
    paint = skia.Paint(Color=WINDOW_TEXT, AntiAlias=True)
    canvas.drawString(text, 10.0, 4.0 + font.getSize(), font, paint)

    # Sunken bevel: dark, dark-dark, light, light-light
    _draw_bevel(canvas, width, height, CONTROL_DARK, CONTROL_DARK_DARK, CONTROL_LIGHT, CONTROL_LIGHT_LIGHT)

    return _surface_to_png_bytes(surface)


def _render_button_image(width, height, caption):
    surface = skia.Surface(width, height)
    canvas = surface.getCanvas()
    canvas.clear(CONTROL)

    font = _make_font(14)
    paint = skia.Paint(Color=WINDOW_TEXT, AntiAlias=True)
    text_width = font.measureText(caption)
    metrics = font.getMetrics()
    text_height = metrics.fDescent - metrics.fAscent
    x = (width - text_width) / 2
    y = (height - text_height) / 2 - metrics.fAscent
    canvas.drawString(caption, x, y, font, paint)

    # Raised bevel: light-light, light, dark, dark-dark
    _draw_bevel(canvas, width, height, CONTROL_LIGHT_LIGHT, CONTROL_LIGHT, CONTROL_DARK, CONTROL_DARK_DARK)

    return _surface_to_png_bytes(surface)


def manage_activex_control_skia_example(global_opts):
    # Accessing the presentation with ActiveX controls
    with slides.Presentation(global_opts.data_dir + "activex_master.pptm") as presentation:
        # Accessing the first slide in presentation
        slide = presentation.slides[0]

        # changing TextBox text
        control = slide.controls[0]

        if control.name == "TextBox1" and control.properties is not None:
            new_text = "Changed text"
            control.properties.remove("Value")
            control.properties.add("Value", new_text)

            # changing substitute image
            # PowerPoint will replace this image during activeX activation, so sometime it's OK to leave image unchanged
            buf = _render_textbox_image(int(control.frame.width), int(control.frame.height), new_text)
            control.substitute_picture_format.picture.image = presentation.images.add_image(buf)
            buf.close()

        # changing Button caption
        control = slide.controls[1]

        if control.name == "CommandButton1" and control.properties is not None:
            new_caption = "MessageBox"
            control.properties.remove("Caption")
            control.properties.add("Caption", new_caption)

            # changing substitute
            buf = _render_button_image(int(control.frame.width), int(control.frame.height), new_caption)
            control.substitute_picture_format.picture.image = presentation.images.add_image(buf)
            buf.close()

        # Moving ActiveX frames 100 points down
        for ctl in slide.controls:
            frame = ctl.frame
            ctl.frame = slides.ShapeFrame(
                frame.x, frame.y + 100, frame.width, frame.height, frame.flip_h, frame.flip_v, frame.rotation)

        # Save the presentation with Edited ActiveX Controls
        presentation.save(global_opts.out_dir + "activex_manage_control-skia-edited_out.pptm", slides.export.SaveFormat.PPTM)

        # Now removing controls
        slide.controls.clear()

        # Saving the presentation with cleared ActiveX controls
        presentation.save(global_opts.out_dir + "activex_manage_control-skia-cleared_out.pptm", slides.export.SaveFormat.PPTM)
