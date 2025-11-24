import io

import aspose.pydrawing as drawing
import aspose.slides as slides


def manage_activex_control(global_opts):
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

            image = drawing.Bitmap(int(control.frame.width), int(control.frame.height))
            with drawing.Graphics.from_image(image) as graphics:
                with drawing.SolidBrush(drawing.Color.from_known_color(drawing.KnownColor.WINDOW)) as brush:
                    graphics.fill_rectangle(brush, 0, 0, image.width, image.height)

                font = drawing.Font("Arial", 14.0)
                with drawing.SolidBrush(drawing.Color.from_known_color(drawing.KnownColor.WINDOW_TEXT)) as brush:
                    graphics.draw_string(new_text, font, brush, 10.0, 4.0)

                with drawing.Pen(drawing.Color.from_known_color(drawing.KnownColor.CONTROL_DARK), 1.0) as pen:
                    graphics.draw_lines(pen, [
                        drawing.PointF(0, image.height - 1), 
                        drawing.PointF(0, 0), 
                        drawing.PointF(image.width - 1, 0)
                    ])

                with drawing.Pen(drawing.Color.from_known_color(drawing.KnownColor.CONTROL_DARK_DARK), 1.0) as pen:
                    graphics.draw_lines(pen, [ 
                        drawing.PointF(1, image.height - 2), 
                        drawing.PointF(1, 1), 
                        drawing.PointF(image.width - 2, 1)
                    ])

                with drawing.Pen(drawing.Color.from_known_color(drawing.KnownColor.CONTROL_LIGHT), 1.0) as pen:
                    graphics.draw_lines(pen, [ 
                        drawing.PointF(1, image.height - 1), 
                        drawing.PointF(image.width - 1, image.height - 1),
                        drawing.PointF(image.width - 1, 1)
                    ])

                with drawing.Pen(drawing.Color.from_known_color(drawing.KnownColor.CONTROL_LIGHT_LIGHT), 1.0) as pen:
                    graphics.draw_lines(pen, [
                        drawing.PointF(0, image.height), 
                        drawing.PointF(image.width, image.height), 
                        drawing.PointF(image.width, 0)
                    ])

            with io.BytesIO() as ms:
                image.save(ms, drawing.imaging.ImageFormat.png)
                ms.seek(0)
                control.substitute_picture_format.picture.image = presentation.images.add_image(ms)

        # changing Button caption
        control = slide.controls[1]

        if control.name == "CommandButton1" and control.properties is not None:
            new_caption = "MessageBox"
            control.properties.remove("Caption")
            control.properties.add("Caption", new_caption)

            # changing substitute
            image = drawing.Bitmap(int(control.frame.width), int(control.frame.height))
            with drawing.Graphics.from_image(image) as graphics:
                with drawing.SolidBrush(drawing.Color.from_known_color(drawing.KnownColor.CONTROL)) as brush:
                    graphics.fill_rectangle(brush, 0, 0, image.width, image.height)

                font = drawing.Font("Arial", 14.0)
                with drawing.SolidBrush(drawing.Color.from_known_color(drawing.KnownColor.WINDOW_TEXT)) as brush:
                    textSize = graphics.measure_string(new_caption, font, 1000)
                    graphics.draw_string(new_caption, font, brush, (image.width - textSize.width) / 2, (image.height - textSize.height) / 2)

                with drawing.Pen(drawing.Color.from_known_color(drawing.KnownColor.CONTROL_LIGHT_LIGHT), 1.0) as pen:
                    graphics.draw_lines(pen, [ 
                        drawing.PointF(0, image.height - 1), 
                        drawing.PointF(0, 0), 
                        drawing.PointF(image.width - 1, 0)
                    ])
                
                with drawing.Pen(drawing.Color.from_known_color(drawing.KnownColor.CONTROL_LIGHT), 1.0) as pen:
                    graphics.draw_lines(pen, [ 
                        drawing.PointF(1, image.height - 2), 
                        drawing.PointF(1, 1), 
                        drawing.PointF(image.width - 2, 1)
                    ])

                with drawing.Pen(drawing.Color.from_known_color(drawing.KnownColor.CONTROL_DARK), 1.0) as pen:
                    graphics.draw_lines(pen, [
                        drawing.PointF(1, image.height - 1),
                        drawing.PointF(image.width - 1, image.height - 1),
                        drawing.PointF(image.width - 1, 1)
                    ])
                
                with drawing.Pen(drawing.Color.from_known_color(drawing.KnownColor.CONTROL_DARK_DARK), 1.0) as pen:
                    graphics.draw_lines(pen, [
                         drawing.PointF(0, image.height), 
                         drawing.PointF(image.width, image.height), 
                         drawing.PointF(image.width, 0)
                    ])

            with io.BytesIO() as ms:
                image.save(ms, drawing.imaging.ImageFormat.png)
                ms.seek(0)
                control.substitute_picture_format.picture.image = presentation.images.add_image(ms)

        # Moving ActiveX frames 100 points down
        for ctl in slide.controls:
            frame = control.frame
            control.frame = slides.ShapeFrame(
                frame.x, frame.y + 100, frame.width, frame.height, frame.flip_h, frame.flip_v, frame.rotation)

        # Save the presentation with Edited ActiveX Controls
        presentation.save(global_opts.out_dir + "activex_manage_control-edited_out.pptm", slides.export.SaveFormat.PPTM)

        # Now removing controls
        slide.controls.clear()

        # Saving the presentation with cleared ActiveX controls
        presentation.save(global_opts.out_dir + "activex_manage_control-cleared_out.pptm", slides.export.SaveFormat.PPTM)
