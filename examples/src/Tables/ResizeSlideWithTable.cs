import aspose.slides as slides
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Tables
{
    class ResizeSlideWithTable
    {
        public static void Run() {

            #ExStart:ResizeSlideWithTable
            Presentation presentation = new Presentation("D:\\Test.pptx")

            #Old slide size
            currentHeight = presentation.SlideSize.size.height
            currentWidth = presentation.SlideSize.size.width

            #Changing slide size
            presentation.SlideSize.type = SlideSizeType.A4Paper
            #presentation.SlideSize.Orientation = SlideOrienation.Portrait

            #New slide size
            newHeight = presentation.SlideSize.size.height
            newWidth = presentation.SlideSize.size.width


            ratioHeight = newHeight / currentHeight
            ratioWidth = newWidth / currentWidth

            foreach (IMasterSlide master in presentation.Masters)
            {
                foreach (IShape shape in master.shapes)
                {
                    #Resize position
                    shape.height = shape.height * ratioHeight
                    shape.width = shape.width * ratioWidth

                    #Resize shape size if required 
                    shape.y = shape.y * ratioHeight
                    shape.x = shape.x * ratioWidth

                }

                foreach (ILayoutSlide layoutslide in master.LayoutSlides)
                {
                    foreach (IShape shape in layoutslide.shapes)
                    {
                        #Resize position
                        shape.height = shape.height * ratioHeight
                        shape.width = shape.width * ratioWidth

                        #Resize shape size if required 
                        shape.y = shape.y * ratioHeight
                        shape.x = shape.x * ratioWidth

                    }

                }
            }

            foreach (slide in presentation.Slides)
            {
                foreach (IShape shape in slide.shapes)
                {
                    #Resize position
                    shape.height = shape.height * ratioHeight
                    shape.width = shape.width * ratioWidth

                    #Resize shape size if required 
                    shape.y = shape.y * ratioHeight
                    shape.x = shape.x * ratioWidth
                    if (shape is ITable)
                    {
                        ITable table = (ITable)shape
                        foreach (IRow row in table.Rows)
                        {
                            row.MinimalHeight = row.MinimalHeight * ratioHeight
                            #   row.height = row.height * ratioHeight
                        }
                        foreach (IColumn col in table.Columns)
                        {
                            col.width = col.width * ratioWidth

                        }
                    }

                }
            }

            presentation.save("D:\\Resize.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:ResizeSlideWithTable

        }
    }
}
