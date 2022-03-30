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
    Worksheet sheet = book.Worksheets[0]
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

        EmfSheetName=dataDir + "test" + sheet.Name + " Page" + (j + 1) + ".out.emf"
        sr.ToImage(j, EmfSheetName)
     
        bytes = File.ReadAllBytes(EmfSheetName)
        emfImage = pres.images.add_image(bytes)
        slide= pres.slides.AddEmptySlide(pres.LayoutSlides.GetByType(SlideLayoutType.Blank))
        m = slide.shapes.AddPictureFrame(ShapeType.Rectangle, 0, 0, pres.SlideSize.size.width, pres.SlideSize.size.height, emfImage)
    }
    
    pres.save(dataDir+"Saved.pptx", slides.export.SaveFormat.PPTX)

       #ExEnd:ImageAsEMF
   }
   }
}
