using System
import aspose.pydrawing as drawing
using System.IO
import aspose.slides as slides
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{

    # This example demonstrates retrieving bullet's fill effective data.

    class BulletFillFormatEffective
    {
        public static void Run()
        {
            dataDir = RunExamples.GetDataDir_Text()
            pptxFile = Path.Combine(dataDir, "BulletData.pptx")

            using (Presentation pres = new Presentation(pptxFile))
            {
                AutoShape autoShape = (AutoShape) pres.slides[0].shapes[0]
                foreach (Paragraph para in autoShape.text_frame.Paragraphs)
                {
                    IBulletFormatEffectiveData bulletFormatEffective = para.ParagraphFormat.Bullet.GetEffective()
                    print("Bullet type: " + bulletFormatEffective.type)
                    if (bulletFormatEffective.type != BulletType.NONE)
                    {
                        print("Bullet fill type: " + bulletFormatEffective.FillFormat.FillType)
                        switch (bulletFormatEffective.FillFormat.FillType)
                        {
                            case slides.FillType.SOLID:
                                print(
                                    "Solid fill color: " + bulletFormatEffective.FillFormat.SolidFillColor)
                                break
                            case FillType.Gradient:
                                print("Gradient stops count: " +
                                                  bulletFormatEffective.FillFormat.GradientFormat.GradientStops.Count)
                                foreach (IGradientStopEffectiveData gradStop in bulletFormatEffective.FillFormat
                                    .GradientFormat.GradientStops)
                                    print(gradStop.Position + ": " + gradStop.Color)
                                break
                            case FillType.Pattern:
                                print("Pattern style: " +
                                                  bulletFormatEffective.FillFormat.PatternFormat.PatternStyle)
                                print("Fore color: " +
                                                  bulletFormatEffective.FillFormat.PatternFormat.ForeColor)
                                print("Back color: " +
                                                  bulletFormatEffective.FillFormat.PatternFormat.BackColor)
                                break
                        }
                    }

                    print()
                }
            }
        }
    }
}
