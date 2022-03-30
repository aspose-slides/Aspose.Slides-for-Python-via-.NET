using System.IO

import aspose.slides as slides
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class AddVideoFrame
    {
        public static void Run()
        {
            #ExStart:AddVideoFrame
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate PrseetationEx class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add Video Frame
                IVideoFrame vf = sld.shapes.AddVideoFrame(50, 150, 300, 150, dataDir+ "video1.avi")

                # Set Play Mode and Volume of the Video
                vf.PlayMode = VideoPlayModePreset.Auto
                vf.Volume = AudioVolumeMode.Loud

                #Write the PPTX file to disk
                pres.save(dataDir + "VideoFrame_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AddVideoFrame
        }
    }
}