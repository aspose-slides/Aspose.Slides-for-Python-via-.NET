using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using Aspose.slides.Util

namespace CSharp.Presentations.properties
{
    public class CheckPasswordExample
    {
        # The example below demonstrates how to check a password to open a presentation

        public static void Run()
        {
            #Path for source presentation
            pptFile = Path.Combine(RunExamples.GetDataDir_PresentationProperties(), "open_pass1.ppt")

            # Check the Password via IPresentationInfo Interface
            IPresentationInfo presentationInfo = PresentationFactory.Instance.GetPresentationInfo(pptFile)
            bool isPasswordCorrect = presentationInfo.CheckPassword("my_password")
            print("The password \"my_password\" for the presentation is " + isPasswordCorrect)
            
            isPasswordCorrect = presentationInfo.CheckPassword("pass1")
            print("The password \"pass1\" for the presentation is " + isPasswordCorrect)
        }
    }
}
