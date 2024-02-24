import aspose.slides as slides
import math


def get_direction(w, h, flip_h, flip_v):
    end_line_x = w * (-1 if flip_h else 1)
    end_line_y = h * (-1 if flip_v else 1)
    end_y_axis_x = 0
    end_y_axis_y = h
    angle = math.atan2(end_y_axis_y, end_y_axis_x) - math.atan2(end_line_y, end_line_x)
    if angle < 0:
         angle += 2 * math.pi
    return angle * 180.0 / math.pi


def connector_line_angle(global_opts):
    with slides.Presentation(global_opts.data_dir + "shapes_connector_line_angle.pptx") as pres:
        slide = pres.slides[0]
        for shape in slide.shapes:
            direction = 0.0
            if type(shape) is slides.AutoShape:
                if shape.shape_type == slides.ShapeType.LINE:
                    direction = get_direction(shape.width, shape.Height, shape.frame.flip_h, shape.frame.flip_v)
            elif type(shape) is slides.Connector:
                direction = get_direction(shape.width, shape.height, shape.frame.flip_h, shape.frame.flip_v)
        print(direction)
