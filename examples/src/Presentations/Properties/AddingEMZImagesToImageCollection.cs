import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/


namespace Aspose.slides.Examples.CSharp.Presentations.properties
{
    public class AddingEMZImagesToImageCollection
    {
        public static void Run()
        {
            #ExStart:AddingEMZImagesToImageCollection
           # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationProperties()
            Presentation p = new Presentation()
               s = p.slides[0]
               # byte[] buffer=new byte()
              imagePath=@"C:\Aspose Data\emf files\"
              byte[] data = GetCompressedData(imagePath + "2.emz")
             if (s != None)
        {
              if (s.shapes != None)
          {
              imgx = p.images.add_image(data)

              m = s.shapes.AddPictureFrame(ShapeType.Rectangle, 0, 0, p.SlideSize.size.width, p.SlideSize.size.height , imgx)
              p.save("C:\\Asopse Data\\Saved.pptx", slides.export.SaveFormat.PPTX)
          }
          }
         }
        

       #private byte[] GetCompressedData(fileNameZip, byte[] buffer)
      private static byte[] GetCompressedData(fileNameZip)
    {
        byte[] bufferZip = None
      /*  byte[] buffer = None

        FileStream f1 = new FileStream(fileName, FileMode.Open)
    byte[] buffer=f1.
        using (FileStream f = new FileStream(fileNameZip, FileMode.Create))
        {
            buffer = new byte[f.Length]
            using (gz = new GZipStream(f, CompressionMode.Compress, False))
            {
                gz.Write(buffer, 0, buffer.Length)
            }
        }
    */
        using (FileStream f = new FileStream(fileNameZip, FileMode.Open))
        {
            bufferZip = new byte[f.Length]
            f.Read(bufferZip, 0, (int)f.Length)
        }

        return bufferZip
        }
            #ExEnd:AddingEMZImagesToImageCollection
        }
    }
