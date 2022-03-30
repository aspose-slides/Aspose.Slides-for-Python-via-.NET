import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Presentations.Saving
{
    class ConvertSvgImageObjectIntoGroupOfShapes
    {
        public static void Run() {

            #ExStart:ConvertSvgImageObjectIntoGroupOfShapes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationSaving()

            using (Presentation pres = new Presentation(dataDir+ "image.pptx"))
            {
                PictureFrame pFrame = pres.slides[0].shapes[0] as PictureFrame
                ISvgImage svgImage = pFrame.PictureFormat.picture.image.SvgImage
                if (svgImage != None)
                {
                    # Convert svg image into group of shapes
                    IGroupShape groupShape = pres.slides[0].shapes.AddGroupShape(svgImage, pFrame.frame.x, pFrame.frame.y,
                        pFrame.frame.width, pFrame.frame.height)
                    # remove source svg image from presentation
                    pres.slides[0].shapes.Remove(pFrame)
                }

                pres.save(dataDir + "image_group.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ConvertSvgImageObjectIntoGroupOfShapes
        }

    }
}
