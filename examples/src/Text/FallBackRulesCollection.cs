import aspose.slides as slides
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class FallBackRulesCollection
    {
        public static void Run()
        {

            #ExStart:FallBackRulesCollection

            with slides.Presentation() as presentation:
            {
                IFontFallBackRulesCollection userRulesList = new FontFallBackRulesCollection()

                userRulesList.add(new FontFallBackRule(0x0B80, 0x0BFF, "Vijaya"))
                userRulesList.add(new FontFallBackRule(0x3040, 0x309F, "MS Mincho, MS Gothic"))

                presentation.FontsManager.FontFallBackRulesCollection = userRulesList
            }
            #ExEnd:FallBackRulesCollection

        }
    }
}
