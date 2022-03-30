using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export

/*
This code example demonstrates how the SetMacroHyperlinkClick method is used to set a macro hyperlink click on a shape:
*/

namespace Aspose.slides.Examples.CSharp.slides.Hyperlinks
{
    public class MacroHyperlink
    {
        public static void Run()
        {
            macroName = "TestMacro"
            with slides.Presentation() as presentation:
            {
                shape = presentation.slides[0].shapes.add_auto_shape(ShapeType.BlankButton, 20, 20, 80, 30)
                shape.HyperlinkManager.SetMacroHyperlinkClick(macroName)

                print("External URL is {0}", shape.HyperlinkClick.ExternalUrl)
                print("Shape action type is {0}", shape.HyperlinkClick.ActionType)
            }
        }
    }
}
