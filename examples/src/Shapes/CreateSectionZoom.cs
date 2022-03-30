using System
import aspose.pydrawing as drawing
using System.IO

import aspose.slides as slides
using Aspose.slides.Export

/*
This sample demonstrates how to create a section zoom using Aspose.Slides for .NET
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class CreateSectionZoom
    {
        public static void Run()
        {
            # Output file name
            resultPath = Path.Combine(RunExamples.OutPath, "SectionZoomPresentation.pptx")

            with slides.Presentation() as pres:
            {
                #Adds a new slide to the presentation
                slide = pres.slides.AddEmptySlide(pres.slides[0].LayoutSlide)
                slide.Background.fill_format.fill_type = slides.FillType.SOLID
                slide.Background.fill_format.solid_fill_color.color = Color.YellowGreen
                slide.Background.type = BackgroundType.OwnBackground

                # Adds a new Section to the presentation
                pres.Sections.AddSection("Section 1", slide)

                # Adds a SectionZoomFrame object
                ISectionZoomFrame sectionZoomFrame = pres.slides[0].shapes.AddSectionZoomFrame(20, 20, 300, 200, pres.Sections[1])

                # Saves the presentation
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
