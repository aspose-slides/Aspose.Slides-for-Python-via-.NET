using System
using System.Collections.Generic
using System.Data
import aspose.pydrawing as drawing
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using DataTable = System.Data.DataTable

namespace CSharp.Presentations.Conversion
{
    # In this example, based on a simple presentation template and a simplified database. We demonstrate the
    # possibility of creating a set of presentations for each of the departments of an imaginary organization.
    # Each of the resulting presentations will include the name of the department, the name of the manager,
    # the staff of the department, and the chart for the schedule of the plan.

    public class MailMergeExample
    {
        public static void Run()
        {
            dataDir = RunExamples.GetDataDir_Conversion()
            presTemplatePath = Path.Combine(dataDir, "PresentationTemplate.pptx")
            resultPath = Path.Combine(RunExamples.OutPath, "MailMergeResult")

            # Path to the data.
            # XML data is one of the examples of the possible MailMerge data sources (among RDBMS and other types of data sources). 
            dataPath = Path.Combine(dataDir, "TestData.xml")

            # Check if result path exists
            if (!Directory.Exists(resultPath))
                Directory.CreateDirectory(resultPath)

            # Creating DataSet using XML data
            using (DataSet dataSet = new DataSet())
            {
                dataSet.ReadXml(dataPath)

                DataTableCollection dataTables = dataSet.Tables
                DataTable usersTable = dataTables["TestTable"]
                DataTable staffListTable = dataTables["StaffList"]
                DataTable planFactTable = dataTables["Plan_Fact"]

                # For all records in main table we will create a separate presentation
                foreach (DataRow userRow in usersTable.Rows)
                {
                    # create result (individual) presentation name
                    presPath = Path.Combine(resultPath, "PresFor_" + userRow["Name"] + ".pptx")

                    # Load presentation template
                    using (Presentation pres = new Presentation(presTemplatePath))
                    {
                        # Fill text boxes with data from data base main table
                        ((AutoShape)pres.slides[0].shapes[0]).text_frame.text =
                            "Chief of the department - " + userRow["Name"]
                        ((AutoShape)pres.slides[0].shapes[4]).text_frame.text = userRow["Department"].ToString()

                        # Get image from data base
                        byte[] bytes = Convert.FromBase64String(userRow["Img"].ToString())

                        # insert image into picture frame of presentation
                        image = pres.images.add_image(bytes)
                        IPictureFrame pf = pres.slides[0].shapes[1] as PictureFrame
                        pf.PictureFormat.picture.image.ReplaceImage(image)

                        # Get abd prepare text frame for filling it with datas
                        list = pres.slides[0].shapes[2] as IAutoShape
                        ITextFrame textFrame = list.text_frame

                        textFrame.Paragraphs.clear()
                        Paragraph para = new Paragraph()
                        para.text = "Department Staff:"
                        textFrame.Paragraphs.add(para)

                        # fill staff data
                        FillStaffList(textFrame, userRow, staffListTable)

                        # fill plan fact data
                        FillPlanFact(pres, userRow, planFactTable)

                        pres.save(presPath, slides.export.SaveFormat.PPTX)
                    }
                }
            }
        }

        #/ <summary>
        #/ Fill text frame with datas from slave table as a list with bullet
        #/ </summary>
        static void FillStaffList(ITextFrame textFrame, DataRow userRow, DataTable staffListTable)
        {
            foreach (DataRow listRow in staffListTable.Rows)
            {
                if (listRow["UserId"].ToString() == userRow["Id"].ToString())
                {
                    Paragraph para = new Paragraph()
                    para.ParagraphFormat.Bullet.type = BulletType.Symbol
                    para.ParagraphFormat.Bullet.Char = Convert.ToChar(8226)
                    para.text = listRow["Name"].ToString()
                    para.ParagraphFormat.Bullet.Color.ColorType = ColorType.RGB
                    para.ParagraphFormat.Bullet.Color.color = Color.Black
                    para.ParagraphFormat.Bullet.IsBulletHardColor = 1
                    para.ParagraphFormat.Bullet.height = 100
                    textFrame.Paragraphs.add(para)
                }
            }
        }

        #/ <summary>
        #/ Fills data chart from the secondary planFact table  
        #/ </summary>
        static void FillPlanFact(Presentation pres, DataRow row, DataTable planFactTable)
        {
            chart = pres.slides[0].shapes[3] as Chart
            IChartTitle chartTitle = chart.chart_title
            chartTitle.text_frame_for_overriding.text = row["Name"] + " : Plan / Fact"

            DataRow[] selRows = planFactTable.Select("UserId = " + row["Id"])
            range = chart.chart_data.get_range()

            cellsFactory = chart.chart_data.chart_data_workbook
            worksheetIndex = 0

            chart.chart_data.series[0].data_points.add_data_point_for_line_series(
                cellsFactory.get_cell(worksheetIndex, 1, 1,
                    double.Parse(selRows[0]["PlanData"].ToString())))
            chart.chart_data.series[1].data_points.add_data_point_for_line_series(
                cellsFactory.get_cell(worksheetIndex, 1, 2,
                    double.Parse(selRows[0]["FactData"].ToString())))

            chart.chart_data.series[0].data_points.add_data_point_for_line_series(
                cellsFactory.get_cell(worksheetIndex, 2, 1,
                    double.Parse(selRows[1]["PlanData"].ToString())))
            chart.chart_data.series[1].data_points.add_data_point_for_line_series(
                cellsFactory.get_cell(worksheetIndex, 2, 2,
                    double.Parse(selRows[1]["FactData"].ToString())))

            chart.chart_data.series[0].data_points.add_data_point_for_line_series(
                cellsFactory.get_cell(worksheetIndex, 3, 1,
                    double.Parse(selRows[2]["PlanData"].ToString())))
            chart.chart_data.series[1].data_points.add_data_point_for_line_series(
                cellsFactory.get_cell(worksheetIndex, 3, 2,
                    double.Parse(selRows[2]["FactData"].ToString())))

            chart.chart_data.series[0].data_points.add_data_point_for_line_series(
                cellsFactory.get_cell(worksheetIndex, 3, 1,
                    double.Parse(selRows[3]["PlanData"].ToString())))
            chart.chart_data.series[1].data_points.add_data_point_for_line_series(
                cellsFactory.get_cell(worksheetIndex, 3, 2,
                    double.Parse(selRows[3]["FactData"].ToString())))

            chart.chart_data.SetRange(range)
        }
    }
}
