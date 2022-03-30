import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Notes
{
	class HeaderAndFooterInNotesSlide
	{
     public static void Run()
		{
			#ExStart:HeaderAndFooterInNotesSlide
			dataDir = RunExamples.GetDataDir_Slides_Presentations_Notes()
			using (Presentation presentation = new Presentation(dataDir + "presentation.pptx"))
			{
				# Change Header and Footer settings for notes master and all notes slides
				IMasterNotesSlide masterNotesSlide = presentation.MasterNotesSlideManager.MasterNotesSlide
				if (masterNotesSlide != None)
				{
					IMasterNotesSlideHeaderFooterManager headerFooterManager = masterNotesSlide.HeaderFooterManager

					headerFooterManager.SetHeaderAndChildHeadersVisibility(True) # make the master notes slide and all child Footer placeholders visible
					headerFooterManager.SetFooterAndChildFootersVisibility(True) # make the master notes slide and all child Header placeholders visible
					headerFooterManager.SetSlideNumberAndChildSlideNumbersVisibility(True) # make the master notes slide and all child SlideNumber placeholders visible
					headerFooterManager.SetDateTimeAndChildDateTimesVisibility(True) # make the master notes slide and all child Date and time placeholders visible

					headerFooterManager.SetHeaderAndChildHeadersText("Header text") # set text to master notes slide and all child Header placeholders
					headerFooterManager.SetFooterAndChildFootersText("Footer text") # set text to master notes slide and all child Footer placeholders
					headerFooterManager.SetDateTimeAndChildDateTimesText("Date and time text") # set text to master notes slide and all child Date and time placeholders
				}

				# Change Header and Footer settings for first notes slide only
				INotesSlide notesSlide = presentation.slides[0].NotesSlideManager.NotesSlide
				if (notesSlide != None)
				{
					INotesSlideHeaderFooterManager headerFooterManager = notesSlide.HeaderFooterManager
					if (!headerFooterManager.IsHeaderVisible)
						headerFooterManager.SetHeaderVisibility(True) # make this notes slide Header placeholder visible

					if (!headerFooterManager.IsFooterVisible)
						headerFooterManager.SetFooterVisibility(True) # make this notes slide Footer placeholder visible

					if (!headerFooterManager.IsSlideNumberVisible)
						headerFooterManager.SetSlideNumberVisibility(True) # make this notes slide SlideNumber placeholder visible

					if (!headerFooterManager.IsDateTimeVisible)
						headerFooterManager.SetDateTimeVisibility(True) # make this notes slide Date-time placeholder visible

					headerFooterManager.SetHeaderText("New header text") # set text to notes slide Header placeholder
					headerFooterManager.SetFooterText("New footer text") # set text to notes slide Footer placeholder
					headerFooterManager.SetDateTimeText("New date and time text") # set text to notes slide Date-time placeholder
				}
				presentation.save(dataDir + "testresult.pptx",slides.export.SaveFormat.PPTX)
			}
		
		  }
		
		#ExEnd:HeaderAndFooterInNotesSlide
	}
}