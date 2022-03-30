import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Drawing.Imaging
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class RenderingWithFallBackFont
    {
        public static void Run()
        {

            #ExStart:RenderingWithFallBackFont

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create new instance of a rules collection
            IFontFallBackRulesCollection rulesList = new FontFallBackRulesCollection()

            # create a number of rules
            rulesList.add(new FontFallBackRule(0x400, 0x4FF, "Times New Roman"))
            #rulesList.add(new FontFallBackRule(...))

            foreach (IFontFallBackRule fallBackRule in rulesList)
            {
                #Trying to remove FallBack font "Tahoma" from loaded rules
                fallBackRule.Remove("Tahoma")

                #And to update of rules for specified range
                if ((fallBackRule.RangeEndIndex >= 0x4000) && (fallBackRule.RangeStartIndex < 0x5000))
                    fallBackRule.AddFallBackFonts("Verdana")
            }

            #Also we can remove any existing rules from list
            if (rulesList.Count > 0)
                rulesList.Remove(rulesList[0])

            using (Presentation pres = new Presentation(dataDir + "input.pptx"))
            {
                #Assigning a prepared rules list for using
                pres.FontsManager.FontFallBackRulesCollection = rulesList

                # Rendering of thumbnail with using of initialized rules collection and saving to PNG
                pres.slides[0].GetThumbnail(1f, 1f).save(dataDir + "Slide_0.png", ImageFormat.Png)
            }
            #ExEnd:RenderingWithFallBackFont

        }
    }
}
