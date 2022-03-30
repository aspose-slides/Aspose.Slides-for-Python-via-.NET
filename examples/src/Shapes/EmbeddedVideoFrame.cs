using System.IO

import aspose.slides as slides
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.shapes 
{
    public class EmbeddedVideoFrame
    {
        public static void Run()
        {
            #ExStart:EmbeddedVideoFrame
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()
            videoDir = RunExamples.GetDataDir_Video()
            resultPath = Path.Combine(RunExamples.OutPath, "VideoFrame_out.pptx")

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)
            # Instantiate Presentation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Embedd vide inside presentation
                IVideo vid = pres.Videos.AddVideo(new FileStream(videoDir + "Wildlife.mp4", FileMode.Open), LoadingStreamBehavior.ReadStreamAndRelease)

                # Add Video Frame
                IVideoFrame vf = sld.shapes.AddVideoFrame(50, 150, 300, 350, vid)

                # Set video to Video Frame
                vf.EmbeddedVideo = vid

                # Set Play Mode and Volume of the Video
                vf.PlayMode = VideoPlayModePreset.Auto
                vf.Volume = AudioVolumeMode.Loud

                # Write the PPTX file to disk
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
            #ExEnd:EmbeddedVideoFrame
        }
    }
}