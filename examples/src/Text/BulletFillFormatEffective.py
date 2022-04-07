import aspose.pydrawing as drawing
import aspose.slides as slides


# This example demonstrates retrieving bullet's fill effective data.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "text_bullet_data.pptx") as pres:
    autoShape =  pres.slides[0].shapes[0]
    for para in autoShape.text_frame.paragraphs:
        bulletFormatEffective = para.paragraph_format.bullet.get_effective()
        print("Bullet type: " + str(bulletFormatEffective.type))
        if bulletFormatEffective.type != slides.BulletType.NONE:
            print("Bullet fill type: " + str(bulletFormatEffective.fill_format.fill_type))
            if bulletFormatEffective.fill_format.fill_type == slides.FillType.SOLID:
                print("Solid fill color: " + str(bulletFormatEffective.fill_format.solid_fill_color))
            elif bulletFormatEffective.fill_format.fill_type == slides.FillType.GRADIENT:
                print("Gradient stops count: " + 
                        str(len(bulletFormatEffective.fill_format.gradient_format.gradient_stops)))
                for gradStop in bulletFormatEffective.fill_format.gradient_format.gradient_stops:
                    print(str(gradStop.position) + ": " + str(gradStop.color))
            elif bulletFormatEffective.fill_format.fill_type == slides.FillType.PATTERN:
                print("Pattern style: " +
                        str(bulletFormatEffective.fill_format.pattern_format.pattern_style))
                print("Fore color: " +
                        str(bulletFormatEffective.fill_format.pattern_format.fore_color))
                print("Back color: " +
                        str(bulletFormatEffective.fill_format.pattern_format.back_color))