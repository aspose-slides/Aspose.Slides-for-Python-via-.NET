
using System.IO
using Aspose.Cells
import aspose.slides as slides
using Aspose.slides.DOM.Ole
using SaveFormat = Aspose.slides.Export.SaveFormat

namespace Aspose.slides.Examples.CSharp.shapes 
{
    public class ChangeOLEObjectData
    {
        public static void Run()
        {
            #ExStart:ChangeOLEObjectData
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            using (Presentation pres = new Presentation(dataDir + "ChangeOLEObjectData.pptx"))
            {
                slide = pres.slides[0]

                OleObjectFrame ole = None

                # Traversing all shapes for Ole frame
                foreach (IShape shape in slide.shapes)
                {
                    if (shape is OleObjectFrame)
                    {
                        ole = (OleObjectFrame) shape
                    }
                }

                if (ole != None)
                {
                    using (MemoryStream msln = new MemoryStream(ole.EmbeddedData.EmbeddedFileData))
                    {
                        # Reading object data in Workbook
                        Workbook Wb = new Workbook(msln)

                        using (MemoryStream msout = new MemoryStream())
                        {
                            # Modifying the workbook data
                            Wb.Worksheets[0].Cells[0, 4].PutValue("E")
                            Wb.Worksheets[0].Cells[1, 4].PutValue(12)
                            Wb.Worksheets[0].Cells[2, 4].PutValue(14)
                            Wb.Worksheets[0].Cells[3, 4].PutValue(15)

                            OoxmlSaveOptions so1 = new OoxmlSaveOptions(Aspose.Cells.SaveFormat.Xlsx)
                            Wb.save(msout, so1)

                            # Changing Ole frame object data
                            IOleEmbeddedDataInfo newData = new OleEmbeddedDataInfo(msout.ToArray(), ole.EmbeddedData.EmbeddedFileExtension)
                            ole.SetEmbeddedData(newData)
                        }
                    }
                }
                pres.save(dataDir + "OleEdit_out.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:ChangeOLEObjectData
        }
    }
}