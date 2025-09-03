import aspose.slides as slides


def brightness_contrast_effect_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "BrightnessContrast.pptx") as pres:
        # Get slide
        slide = pres.slides[0]

        # Get picture frame
        picture_frame = slide.shapes[0]

        # Get image transform operations
        image_transform = picture_frame.picture_format.picture.image_transform
        for effect in image_transform:
            if type(effect) is slides.effects.IBrightnessContrast:
                # Get brightness and contrast values
                brightness_contrast_data = effect.get_effective()
                print("Brightness value =", brightness_contrast_data.brightness)
                print("Contrast value =", brightness_contrast_data.contrast)
