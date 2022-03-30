import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Vba
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.VBA
{
    class ExtractingVBAMacros
    {
        public static void Run()
        {
            #ExStart:ExtractingVBAMacros

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_VBA()

            using (Presentation pres = new Presentation(dataDir + "VBA.pptm"))
            {
                if (pres.VbaProject != None) # check if Presentation contains VBA Project
                {
                    foreach (IVbaModule module in pres.VbaProject.Modules)
                    {
                        print(module.Name)
                        print(module.SourceCode)
                    }
                }
            }

            #ExEnd:ExtractingVBAMacros

        }
    }
}
