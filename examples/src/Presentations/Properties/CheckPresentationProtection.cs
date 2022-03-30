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
    class CheckPresentationProtection
    {
        public static void Run()
        {
            #Path for source presentation
            pptxFile = Path.Combine(RunExamples.GetDataDir_PresentationProperties(), "modify_pass2.pptx")
            pptFile = Path.Combine(RunExamples.GetDataDir_PresentationProperties(), "open_pass1.ppt")

            # Check the Write Protection Password via IPresentationInfo Interface
            IPresentationInfo presentationInfo = PresentationFactory.Instance.GetPresentationInfo(pptxFile)
            bool isWriteProtectedByPassword = presentationInfo.IsWriteProtected == 1 && presentationInfo.CheckWriteProtection("pass2")
            print("Is presentation write protected by password = " + isWriteProtectedByPassword)

            # Check the Write Protection Password via IProtectionManager Interface
            using (presentation = new Presentation(pptxFile))
            {
                bool isWriteProtected = presentation.ProtectionManager.CheckWriteProtection("pass2")
                print("Is presentation write protected = " + isWriteProtected)
            }

            # Check Presentation Open Protection via IPresentationInfo Interface
            presentationInfo = PresentationFactory.Instance.GetPresentationInfo(pptFile)
            if (presentationInfo.IsPasswordProtected)
            {
                print("The presentation '" + pptxFile + "' is protected by password to open.")
            }
        }
    }
}
