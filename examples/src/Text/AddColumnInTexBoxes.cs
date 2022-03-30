using System.IO

import aspose.slides as slides
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class AddColumnInTexBoxes
    {
        public static void Run()
        {
            # ExStart:AddColumnInTexBoxes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()
            with slides.Presentation() as presentation:
{
           # Get the first slide of presentation
            slide = presentation.slides[0]

          # Add an AutoShape of Rectangle type
            aShape = slide.shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 300, 300)

        # Add TextFrame to the Rectangle
           aShape.AddTextFrame("All these columns are limited to be within a single text container -- " +
        "you can add or delete text and the new or remaining text automatically adjusts " +
        "itself to flow within the container. You cannot have text flow from one container " +
        "to other though -- we told you PowerPoint's column options for text are limited!")

       # Get text format of TextFrame
        ITextFrameFormat format = aShape.text_frame.TextFrameFormat

      # Specify number of columns in TextFrame
        format.ColumnCount = 3

     # Specify spacing between columns
        format.ColumnSpacing = 10

    # Save created presentation
       presentation.save("ColumnCount.pptx", slides.export.SaveFormat.PPTX)

            }
         
            }
        # ExEnd:AddColumnInTexBoxes
    }
}