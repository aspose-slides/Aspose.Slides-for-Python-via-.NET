import aspose.pydrawing as drawing
import aspose.slides as slides

# This example demonstrates creating 3D shape and appliing 3D effects to the text in it.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    # Create shape and text frame
    shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 314, 122, 400, 215.433)

    textFrame = shape.text_frame

    portion = textFrame.paragraphs[0].portions[0]
    portion.text = "Aspose.Slides"
    fontData = slides.FontData("Arial Black")
    portion.portion_format.latin_font = fontData
    portion.portion_format.font_height = 36

    # Set format of the text
    portion.portion_format.fill_format.fill_type = slides.FillType.PATTERN
    portion.portion_format.fill_format.pattern_format.fore_color.color = drawing.Color.dark_orange
    portion.portion_format.fill_format.pattern_format.back_color.color = drawing.Color.white
    portion.portion_format.fill_format.pattern_format.pattern_style = slides.PatternStyle.SMALL_GRID

    portion.portion_format.line_format.fill_format.fill_type = slides.FillType.SOLID
    portion.portion_format.line_format.fill_format.solid_fill_color.color = drawing.Color.black

    # Add a shadow effect for the text
    portion.portion_format.effect_format.enable_outer_shadow_effect()
    portion.portion_format.effect_format.outer_shadow_effect.shadow_color.color = drawing.Color.black
    portion.portion_format.effect_format.outer_shadow_effect.scale_horizontal = 100
    portion.portion_format.effect_format.outer_shadow_effect.scale_vertical = 65
    portion.portion_format.effect_format.outer_shadow_effect.blur_radius = 4.73
    portion.portion_format.effect_format.outer_shadow_effect.direction = 230
    portion.portion_format.effect_format.outer_shadow_effect.distance = 2
    portion.portion_format.effect_format.outer_shadow_effect.skew_horizontal = 30
    portion.portion_format.effect_format.outer_shadow_effect.skew_vertical = 0
    portion.portion_format.effect_format.outer_shadow_effect.shadow_color.color_transform.add(slides.ColorTransformOperation.SET_ALPHA, 0.32)

    # Add reflection
    portion.portion_format.effect_format.enable_reflection_effect()
    portion.portion_format.effect_format.reflection_effect.blur_radius = 0.5
    portion.portion_format.effect_format.reflection_effect.distance = 4.72
    portion.portion_format.effect_format.reflection_effect.start_pos_alpha = 0
    portion.portion_format.effect_format.reflection_effect.end_pos_alpha = 60
    portion.portion_format.effect_format.reflection_effect.direction = 90
    portion.portion_format.effect_format.reflection_effect.scale_horizontal = 100
    portion.portion_format.effect_format.reflection_effect.scale_vertical = -100
    portion.portion_format.effect_format.reflection_effect.start_reflection_opacity = 60
    portion.portion_format.effect_format.reflection_effect.end_reflection_opacity = 0.9
    portion.portion_format.effect_format.reflection_effect.rectangle_align = slides.RectangleAlignment.BOTTOM_LEFT

    # Add glow effect
    portion.portion_format.effect_format.enable_glow_effect()
    portion.portion_format.effect_format.glow_effect.color.r = 255
    portion.portion_format.effect_format.glow_effect.color.color_transform.add(slides.ColorTransformOperation.SET_ALPHA, 0.54)
    portion.portion_format.effect_format.glow_effect.radius = 7

    # Add transformation
    textFrame.text_frame_format.transform = slides.TextShapeType.ARCH_UP_POUR

    # Add 3D effects to the shape
    shape.three_dformat.bevel_bottom.bevel_type = slides.BevelPresetType.CIRCLE
    shape.three_dformat.bevel_bottom.height = 10.5
    shape.three_dformat.bevel_bottom.width = 10.5

    shape.three_dformat.bevel_top.bevel_type = slides.BevelPresetType.CIRCLE
    shape.three_dformat.bevel_top.height = 12.5
    shape.three_dformat.bevel_top.width = 11

    shape.three_dformat.extrusion_color.color = drawing.Color.orange
    shape.three_dformat.extrusion_height = 6

    shape.three_dformat.contour_color.color = drawing.Color.dark_red
    shape.three_dformat.contour_width = 1.5

    shape.three_dformat.depth = 3

    shape.three_dformat.material = slides.MaterialPresetType.PLASTIC

    shape.three_dformat.light_rig.direction = slides.LightingDirection.TOP
    shape.three_dformat.light_rig.light_type = slides.LightRigPresetType.BALANCED
    shape.three_dformat.light_rig.set_rotation(0, 0, 40)

    shape.three_dformat.camera.camera_type = slides.CameraPresetType.PERSPECTIVE_CONTRASTING_RIGHT_FACING

    # Add 3D effects to the text
    textFrame = shape.text_frame

    textFrame.text_frame_format.three_dformat.bevel_bottom.bevel_type = slides.BevelPresetType.CIRCLE
    textFrame.text_frame_format.three_dformat.bevel_bottom.height = 3.5
    textFrame.text_frame_format.three_dformat.bevel_bottom.width = 3.5

    textFrame.text_frame_format.three_dformat.bevel_top.bevel_type = slides.BevelPresetType.CIRCLE
    textFrame.text_frame_format.three_dformat.bevel_top.height = 12.5
    textFrame.text_frame_format.three_dformat.bevel_top.width = 11

    textFrame.text_frame_format.three_dformat.extrusion_color.color = drawing.Color.orange
    textFrame.text_frame_format.three_dformat.extrusion_height = 6

    textFrame.text_frame_format.three_dformat.contour_color.color = drawing.Color.dark_red
    textFrame.text_frame_format.three_dformat.contour_width = 1.5

    textFrame.text_frame_format.three_dformat.depth = 3

    textFrame.text_frame_format.three_dformat.material = slides.MaterialPresetType.PLASTIC

    textFrame.text_frame_format.three_dformat.light_rig.direction = slides.LightingDirection.TOP
    textFrame.text_frame_format.three_dformat.light_rig.light_type = slides.LightRigPresetType.BALANCED
    textFrame.text_frame_format.three_dformat.light_rig.set_rotation(0, 0, 40)

    textFrame.text_frame_format.three_dformat.camera.camera_type = slides.CameraPresetType.PERSPECTIVE_CONTRASTING_RIGHT_FACING

    pres.save(outDir + "text_three_dformat_out.pptx", slides.export.SaveFormat.PPTX)
