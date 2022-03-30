﻿using Aspose.slides.SmartArt
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    class ChangeSmartArtShapeColorStyle
    {
        public static void Run()
        {
            #ExStart:ChangeSmartArtShapeColorStyle
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            using (Presentation presentation = new Presentation(dataDir + "AccessSmartArtShape.pptx"))
            {
                # Traverse through every shape inside first slide
                foreach (IShape shape in presentation.slides[0].shapes)
                {
                    # Check if shape is of SmartArt type
                    if (shape is ISmartArt)
                    {
                        # Typecast shape to SmartArtEx
                        ISmartArt smart = (ISmartArt)shape

                        # Checking SmartArt color type
                        if (smart.ColorStyle == SmartArtColorType.ColoredFillAccent1)
                        {
                            # Changing SmartArt color type
                            smart.ColorStyle = SmartArtColorType.ColorfulAccentColors
                        }
                    }
                }

                # Saving Presentation
                presentation.save(dataDir + "ChangeSmartArtColorStyle_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ChangeSmartArtShapeColorStyle
        }
    }
}
