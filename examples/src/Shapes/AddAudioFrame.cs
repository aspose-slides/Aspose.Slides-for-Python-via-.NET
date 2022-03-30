using System.IO

import aspose.slides as slides
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class AddAudioFrame
    {
        public static void Run()
        {
            #ExStart:AddAudioFrame
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Prseetation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Load the wav sound file to stram
                FileStream fstr = new FileStream(dataDir+ "sampleaudio.wav", FileMode.Open, FileAccess.Read)

                # Add Audio Frame
                IAudioFrame audioFrame = sld.shapes.AddAudioFrameEmbedded(50, 150, 100, 100, fstr)

                # Set Audio to play across the slides
                audioFrame.PlayAcrossSlides = True

                # Set Audio to automatically rewind to start after playing
                audioFrame.RewindAudio = True
                
                # Set Play Mode and Volume of the Audio
                audioFrame.PlayMode = AudioPlayModePreset.Auto
                audioFrame.Volume = AudioVolumeMode.Loud

                #Write the PPTX file to disk
                pres.save(dataDir + "AudioFrameEmbed_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AddAudioFrame
        }
    }
}