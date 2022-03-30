using System.IO

import aspose.slides as slides
using System.Drawing.Imaging
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class DefaultFonts
    {
        public static void Run()
        {
            #ExStart:DefaultFonts
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Use load options to define the default regualr and asian fonts# Use load options to define the default regualr and asian fonts
            loadOptions = slides.LoadOptions(LoadFormat.Auto)
            loadOptions.DefaultRegularFont = "Wingdings"
            loadOptions.DefaultAsianFont = "Wingdings"

            # Load the presentation
            using (Presentation pptx = new Presentation(dataDir + "DefaultFonts.pptx", loadOptions))
            {
                # Generate slide thumbnail
                pptx.slides[0].GetThumbnail(1, 1).save(dataDir + "output_out.png", ImageFormat.Png)

                # Generate PDF
                pptx.save(dataDir + "output_out.pdf", SaveFormat.Pdf)

                # Generate XPS
                pptx.save(dataDir + "output_out.xps", SaveFormat.Xps)
            }
            #ExEnd:DefaultFonts
        }
    }
}