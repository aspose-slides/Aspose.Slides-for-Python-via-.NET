import aspose.pydrawing as drawing
using System.IO

import aspose.slides as slides
using Aspose.slides.Export

/*
This example demonstrates how to create a zoom frame with different images 
and shows how to change the formatting of a zoom frame.
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class CreateZoomFrame
    {
        public static void Run()
        {
            # Output file name
            resultPath = Path.Combine(RunExamples.OutPath, "ZoomFramePresentation.pptx")

            # Path to source image
            imagePath = Path.Combine(RunExamples.GetDataDir_Shapes(), "aspose-logo.jpg")

            with slides.Presentation() as pres:
            {
                #Add new slides to the presentation
                slide2 = pres.slides.AddEmptySlide(pres.slides[0].LayoutSlide)
                slide3 = pres.slides.AddEmptySlide(pres.slides[0].LayoutSlide)

                # Create a background for the second slide
                slide2.Background.type = BackgroundType.OwnBackground
                slide2.Background.fill_format.fill_type = slides.FillType.SOLID
                slide2.Background.fill_format.solid_fill_color.color = Color.Cyan

                # Create a text box for the second slide
                autoshape = slide2.shapes.add_auto_shape(ShapeType.Rectangle, 100, 200, 500, 200)
                autoshape.text_frame.text = "Second Slide"

                # Create a background for the third slide
                slide3.Background.type = BackgroundType.OwnBackground
                slide3.Background.fill_format.fill_type = slides.FillType.SOLID
                slide3.Background.fill_format.solid_fill_color.color = Color.DarkKhaki

                # Create a text box for the third slide
                autoshape = slide3.shapes.add_auto_shape(ShapeType.Rectangle, 100, 200, 500, 200)
                autoshape.text_frame.text = "Trird Slide"

                # Add ZoomFrame objects with slide preview
                zoomFrame1 = pres.slides[0].shapes.AddZoomFrame(20, 20, 250, 200, slide2)

                # Add ZoomFrame objects with custom image
                # Create a new image for the zoom object
                image = pres.images.add_image(Image.FromFile(imagePath))
                zoomFrame2 = pres.slides[0].shapes.AddZoomFrame(200, 250, 250, 100, slide3, image)

                # Set a zoom frame format for the zoomFrame2 object
                zoomFrame2.line_format.width = 5
                zoomFrame2.line_format.fill_format.fill_type = slides.FillType.SOLID
                zoomFrame2.line_format.fill_format.solid_fill_color.color = Color.HotPink
                zoomFrame2.line_format.dash_style = slides.LineDashStyle.DASH_DOT

                # Do not show background for zoomFrame1 object
                zoomFrame1.ShowBackground = False


                # Save the presentation
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
