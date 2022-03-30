using System
import aspose.pydrawing as drawing
using System.IO

import aspose.slides as slides
using Aspose.slides.Export

/*
This sample demonstrates how to create a summary zoom using Aspose.Slides for .NET
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class CreateSummaryZoom
    {
        public static void Run()
        {
            # Output file name
            resultPath = Path.Combine(RunExamples.OutPath, "SummaryZoomPresentation.pptx")

            with slides.Presentation() as pres:
            {
                #Adds a new slide to the presentation
                slide = pres.slides.AddEmptySlide(pres.slides[0].LayoutSlide)
                slide.Background.fill_format.fill_type = slides.FillType.SOLID
                slide.Background.fill_format.solid_fill_color.color = Color.Brown
                slide.Background.type = BackgroundType.OwnBackground

                # Adds a new section to the presentation
                pres.Sections.AddSection("Section 1", slide)

                #Adds a new slide to the presentation
                slide = pres.slides.AddEmptySlide(pres.slides[0].LayoutSlide)
                slide.Background.fill_format.fill_type = slides.FillType.SOLID
                slide.Background.fill_format.solid_fill_color.color = Color.Aqua
                slide.Background.type = BackgroundType.OwnBackground

                # Adds a new section to the presentation
                pres.Sections.AddSection("Section 2", slide)

                #Adds a new slide to the presentation
                slide = pres.slides.AddEmptySlide(pres.slides[0].LayoutSlide)
                slide.Background.fill_format.fill_type = slides.FillType.SOLID
                slide.Background.fill_format.solid_fill_color.color = Color.Chartreuse
                slide.Background.type = BackgroundType.OwnBackground

                # Adds a new section to the presentation
                pres.Sections.AddSection("Section 3", slide)

                #Adds a new slide to the presentation
                slide = pres.slides.AddEmptySlide(pres.slides[0].LayoutSlide)
                slide.Background.fill_format.fill_type = slides.FillType.SOLID
                slide.Background.fill_format.solid_fill_color.color = drawing.Color.dark_green
                slide.Background.type = BackgroundType.OwnBackground

                # Adds a new section to the presentation
                pres.Sections.AddSection("Section 4", slide)

                # Adds a SummaryZoomFrame object
                ISummaryZoomFrame summaryZoomFrame = pres.slides[0].shapes.AddSummaryZoomFrame(150, 50, 300, 200)

                # Saves the presentation
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
