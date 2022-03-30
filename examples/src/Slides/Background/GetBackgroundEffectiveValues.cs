import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Background
{
    class GetBackgroundEffectiveValues
    {

        public static void Run()
        {
            #ExStart:GetBackgroundEffectiveValues
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Background()

            # Instantiate the Presentation class that represents the presentation file
            Presentation pres = new Presentation(dataDir + "SamplePresentation.pptx")

            IBackgroundEffectiveData effBackground = pres.slides[0].Background.GetEffective()

            if (effBackground.fill_format.fill_type == slides.FillType.SOLID)
                print("Fill color: " + effBackground.FillFormat.SolidFillColor)
            else
                print("Fill type: " + effBackground.FillFormat.FillType)

            #ExEnd:GetBackgroundEffectiveValues
        }

    }
}
