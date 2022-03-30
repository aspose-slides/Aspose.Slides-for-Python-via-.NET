using System
import aspose.pydrawing as drawing
using System.Drawing.Imaging
using System.IO
import aspose.slides as slides
using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
Install it and then add its reference to this project. For any issues, questions or suggestions 
Please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.text
{
    public class ManageEmbeddedFonts
    {
        public static void Run()
        {
            #ExStart:ManageEmbeddedFonts
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Instantiate a Presentation object that represents a presentation file
            using (Presentation presentation = new Presentation(dataDir + "EmbeddedFonts.pptx"))
            {
                # render a slide that contains a text frame that uses embedded "FunSized"
                presentation.slides[0].get_thumbnail(new Size(960, 720)).save(dataDir + "picture1_out.png", drawing.imaging.ImageFormat.png)

                IFontsManager fontsManager = presentation.FontsManager

                # get all embedded fonts
                IFontData[] embeddedFonts = fontsManager.GetEmbeddedFonts()

                # find "Calibri" font
                IFontData funSizedEmbeddedFont = Array.Find(embeddedFonts, delegate(IFontData data)
                {
                    return data.FontName == "Calibri"
                })

                # remove "Calibri" font
                fontsManager.RemoveEmbeddedFont(funSizedEmbeddedFont)

                # render the presentation removed "Calibri" font is replaced to an existing one
                presentation.slides[0].get_thumbnail(new Size(960, 720)).save(dataDir + "picture2_out.png", drawing.imaging.ImageFormat.png)

                # save the presentation without embedded "Calibri" font
                presentation.save(dataDir + "WithoutManageEmbeddedFonts_out.ppt", SaveFormat.Ppt)
            }
            #ExEnd:ManageEmbeddedFonts
        }
    }
}