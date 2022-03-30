import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Presentations.Saving
{
    class AddBlobImageToPresentation
    {
        public static void Run() {

            #ExStart:AddBlobImageToPresentation

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationSaving()

            pathToLargeImage = dataDir + "large_image.jpg"

            # create a new presentation which will contain this image
            with slides.Presentation() as pres:
            {
                using (FileStream fileStream = new FileStream(pathToLargeImage, FileMode.Open))
                {
                    # let's add the image to the presentation - we choose KeepLocked behavior, because we not
                    # have an intent to access the "largeImage.png" file.
                    img = pres.images.add_image(fileStream, LoadingStreamBehavior.KeepLocked)
                    pres.slides[0].shapes.AddPictureFrame(ShapeType.Rectangle, 0, 0, 300, 200, img)

                    # save the presentation. Despite that the output presentation will be
                    # large, the memory consumption will be low the whole lifetime of the pres object
                    pres.save(dataDir + "presentationWithLargeImage.pptx", slides.export.SaveFormat.PPTX)
                }
            }

            #ExEnd:AddBlobImageToPresentation

        }
    }
}
