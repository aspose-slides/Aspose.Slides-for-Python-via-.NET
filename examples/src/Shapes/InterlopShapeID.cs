using System.IO

import aspose.slides as slides
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.shapes
{
  class InterlopShapeID
   {  
        #ExStart:InterlopShapeID
        public static void Run()
        {
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            using (Presentation presentation = new Presentation("Presentation.pptx"))
         {
            # Getting unique shape identifier in slide scope
            long officeInteropShapeId = presentation.slides[0].shapes[0].OfficeInteropShapeId
   
            #ExEnd:InterlopShapeID
            }
            }
        }
    }
