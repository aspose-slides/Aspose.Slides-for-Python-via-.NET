import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Rendering_Printing
{
    class SupportOfDigitalSignature
    {

        public static void Run() {

            #ExStart:SupportOfDigitalSignature

            dataDir = RunExamples.GetDataDir_Rendering()
            outPath = RunExamples.OutPath

            with slides.Presentation() as pres:
            {
                
                DigitalSignature signature = new DigitalSignature(dataDir + "testsignature1.pfx", @"testpass1")

                
                signature.Comments = "Aspose.Slides digital signing test."

                
                pres.DigitalSignatures.add(signature)


                pres.save(outPath + "SomePresentationSigned.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:SupportOfDigitalSignature



        }
    }
}
