using System.IO

import aspose.slides as slides
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class LoadExternalFont

    {
        public static void Run()
        {
            # ExStart:LoadExternalFont

            # The path to the documents directory.

            dataDir = RunExamples.GetDataDir_Text()


            # loading presentation uses SomeFont which is not installed on the system
            with slides.Presentation() as pres:
            {
                # load SomeFont from file into the byte array

                byte[] fontData = File.ReadAllBytes(dataDir + "CustomFonts.ttf")

                # load font represented as byte array
                FontsLoader.LoadExternalFont(fontData)

                # font SomeFont will be available during the rendering or other operations
            }
        }

        # ExEnd:LoadExternalFont

    }
}

