import io

from PIL import Image, ImageDraw, ImageFont

import aspose.slides as slides

WINDOW = (255, 255, 255)
WINDOW_TEXT = (0, 0, 0)
CONTROL = (240, 240, 240)
CONTROL_DARK = (160, 160, 160)
CONTROL_DARK_DARK = (105, 105, 105)
CONTROL_LIGHT = (227, 227, 227)
CONTROL_LIGHT_LIGHT = (255, 255, 255)


def _load_font(size=14):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        # Fall back to any DejaVu font commonly present on Linux, then to default
        try:
            return ImageFont.truetype("DejaVuSans.ttf", size)
        except OSError:
            return ImageFont.load_default()


def _draw_bevel(draw, width, height, outer_color, mid_color, inner_color, innermost_color):
    """
    Draws a 4-line 3D bevel border using two nested 'L' shaped polylines per side
    """
    # Outer-most line: bottom-left -> top-left -> top-right
    draw.line(
        [(0, height - 1), (0, 0), (width - 1, 0)],
        fill=outer_color,
        width=1,
    )
    # Second line, inset by 1px
    draw.line(
        [(1, height - 2), (1, 1), (width - 2, 1)],
        fill=mid_color,
        width=1,
    )
    # Third line: bottom-left -> bottom-right -> top-right, inset by 1px
    draw.line(
        [(1, height - 1), (width - 1, height - 1), (width - 1, 1)],
        fill=inner_color,
        width=1,
    )
    # Outer-most line on the opposite side
    draw.line(
        [(0, height), (width, height), (width, 0)],
        fill=innermost_color,
        width=1,
    )


def _render_textbox_image(width, height, text):
    image = Image.new("RGB", (width, height), WINDOW)
    draw = ImageDraw.Draw(image)
    font = _load_font(14)

    draw.text((10.0, 4.0), text, fill=WINDOW_TEXT, font=font)

    # Sunken bevel: dark, dark-dark, light, light-light (outer to inner-ish)
    _draw_bevel(draw, width, height, CONTROL_DARK, CONTROL_DARK_DARK, CONTROL_LIGHT, CONTROL_LIGHT_LIGHT)

    buf = io.BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return buf


def _render_button_image(width, height, caption):
    image = Image.new("RGB", (width, height), CONTROL)
    draw = ImageDraw.Draw(image)
    font = _load_font(14)

    bbox = draw.textbbox((0, 0), caption, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.text((x, y), caption, fill=WINDOW_TEXT, font=font)

    # Raised bevel: light-light, light, dark, dark-dark (outer to inner-ish)
    _draw_bevel(draw, width, height, CONTROL_LIGHT_LIGHT, CONTROL_LIGHT, CONTROL_DARK, CONTROL_DARK_DARK)

    buf = io.BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return buf


def manage_activex_control_pillow_example(global_opts):
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
        presentation.save(global_opts.out_dir + "activex_manage_control-pillow-edited_out.pptm", slides.export.SaveFormat.PPTM)

        # Now removing controls
        slide.controls.clear()

        # Saving the presentation with cleared ActiveX controls
        presentation.save(global_opts.out_dir + "activex_manage_control-pillow-cleared_out.pptm", slides.export.SaveFormat.PPTM)
