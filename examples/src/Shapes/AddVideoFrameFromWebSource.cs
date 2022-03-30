using System
using System.Net
import aspose.slides as slides
using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    class AddVideoFrameFromWebSource
    {
        #ExStart:AddVideoFrameFromWebSource
        public static void Run()
        {
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            with slides.Presentation() as pres:
            {
                AddVideoFromYouTube(pres, "Tj75Arhq5ho")
                pres.save(dataDir + "AddVideoFrameFromWebSource_out.pptx", slides.export.SaveFormat.PPTX)
            }
        }

        private static void AddVideoFromYouTube(Presentation pres, videoId)
        {
            #add videoFrame
            IVideoFrame videoFrame = pres.slides[0].shapes.AddVideoFrame(10, 10, 427, 240, "https:#www.youtube.com/embed/" + videoId)
            videoFrame.PlayMode = VideoPlayModePreset.Auto

            #load thumbnail
            using (WebClient client = new WebClient())
            {
                thumbnailUri = "http:#img.youtube.com/vi/" + videoId + "/hqdefault.jpg"
                videoFrame.PictureFormat.picture.image = pres.images.add_image(client.DownloadData(thumbnailUri))
            }
        }
        #ExEnd:AddVideoFrameFromWebSource
    }
}



