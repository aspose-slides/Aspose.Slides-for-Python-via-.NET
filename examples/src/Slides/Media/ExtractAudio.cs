import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Media
{
    class ExtractAudio
    {
        public static void Run() {

            #ExStart:ExtractAudio

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Media()

            presName = dataDir + "AudioSlide.ppt"
           
            # Instantiate Presentation class that represents the presentation file
            Presentation pres = new Presentation(presName)

            # Access the desired slide
            slide = pres.slides[0]

            # Get the slideshow transition effects for slide
            ISlideShowTransition transition = slide.SlideShowTransition

            #Extract sound in byte array
            byte[] audio = transition.Sound.BinaryData

            print("Length: " + audio.Length)
            #ExEnd:ExtractAudio

        }
    }
}
