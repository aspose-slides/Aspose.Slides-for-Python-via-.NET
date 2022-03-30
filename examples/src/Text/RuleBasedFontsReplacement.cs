import aspose.pydrawing as drawing
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.text
{
    class RuleBasedFontsReplacement
    {
        public static void Run()
        {
            #ExStart:RuleBasedFontsReplacement
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Load presentation
            Presentation presentation = new Presentation(dataDir + "Fonts.pptx")

            # Load source font to be replaced
            IFontData sourceFont = slides.FontData("SomeRareFont")

            # Load the replacing font
            IFontData destFont = slides.FontData("Arial")

            # Add font rule for font replacement
            IFontSubstRule fontSubstRule = new FontSubstRule(sourceFont, destFont, FontSubstCondition.WhenInaccessible)

            # Add rule to font substitute rules collection
            IFontSubstRuleCollection fontSubstRuleCollection = new FontSubstRuleCollection()
            fontSubstRuleCollection.add(fontSubstRule)

            # Add font rule collection to rule list
            presentation.FontsManager.FontSubstRuleList = fontSubstRuleCollection

            # Arial font will be used instead of SomeRareFont when inaccessible
            bmp = presentation.slides[0].get_thumbnail(1f, 1f)

            # Save the image to disk in JPEG format
            bmp.save(dataDir + "Thumbnail_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg)
            #ExEnd:RuleBasedFontsReplacement
        }
    }
}