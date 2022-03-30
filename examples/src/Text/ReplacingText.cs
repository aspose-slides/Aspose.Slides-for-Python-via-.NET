using System.IO

import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.text
{
    public class ReplacingText
    {
        public static void Run()
        {
            #ExStart:ReplacingText
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Instantiate Presentation class that represents PPTX# Instantiate Presentation class that represents PPTX
            using (Presentation pres = new Presentation(dataDir + "ReplacingText.pptx"))
            {

                # Access first slide
                sld = pres.slides[0]

                # Iterate through shapes to find the placeholder
                foreach (IShape shp in sld.shapes)
                    if (shp.Placeholder != None)
                    {
                        # Change the text of each placeholder
                        ((IAutoShape)shp).text_frame.text = "This is Placeholder"
                    }

                # Save the PPTX to Disk
                pres.save(dataDir + "output_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ReplacingText
        }
    }
}