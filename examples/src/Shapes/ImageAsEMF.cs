using System
using System.Collections.Generic
using System.Linq
using System.text
using System.IO
import aspose.slides as slides
using Aspose.Cells
using Aspose.Cells.Drawing
using Aspose.slides.Examples
using Aspose.slides.Examples.CSharp
using Aspose.Cells.Rendering
namespace CSharp.shapes
{
   public  class ImageAsEMF
    {
   public static void Run()
   {
       dataDir = RunExamples.GetDataDir_Shapes()
      #ExStart:ImageAsEMF
    Workbook book = new Workbook(dataDir + "chart.xlsx")
    Worksheet sheet = book.worksheets[0]
    Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions()
    options.HorizontalResolution = 200
    options.VerticalResolution = 200
    options.ImageType = ImageType.Emf

    #Save the workbook to stream
    SheetRender sr = new SheetRender(sheet, options)
    with slides.Presentation() as pres:
    pres.slides.remove_at(0)

    EmfSheetName=""
    for (j = 0 j < sr.PageCount j++)
    {

        EmfSheetName=dataDir + "test" + sheet.name + " Page" + (j + 1) + ".out.emf"
        sr.ToImage(j, EmfSheetName)
     
        bytes = File.ReadAllBytes(EmfSheetName)
        emfImage = pres.images.add_image(bytes)
        slide= pres.slides.add_empty_slide(pres.layout_slides.get_by_type(slides.SlideLayoutType.BLANK))
        m = slide.shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 0, 0, pres.slide_size.size.width, pres.slide_size.size.height, emfImage)
    }
    
    pres.save(dataDir+"Saved.pptx", slides.export.SaveFormat.PPTX)

       #ExEnd:ImageAsEMF
   }
   }
}
