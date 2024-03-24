import os
import shutil
import subprocess
import argparse

import aspose.slides as slides
import aspose.pydrawing as drawing


class Pptx2VideoConverter:
    _IMAGE_FILE_TEMPLATE = "frame_%d.png"

    def __init__(self, presentation, out_video_path, temp_folder_path, fps):
        self.presentation = presentation
        self.out_video_path = out_video_path
        self.temp_folder_path = temp_folder_path
        self.fps = fps

        try:
            shutil.rmtree(self.temp_folder_path)
        except FileNotFoundError:
            pass

        os.makedirs(self.temp_folder_path)
        os.makedirs(os.path.dirname(self.out_video_path), exist_ok=True)

    def generate_frames(self):
        with slides.export.experimental.SimplePresentationFramesGenerator(self.presentation, self.fps) as frames_generator:
            for frame_args in frames_generator.enumerate_frames(self.presentation.slides):
                image_file_name = self._IMAGE_FILE_TEMPLATE % frame_args.frames_generator.frame_index
                full_image_path = os.path.join(self.temp_folder_path, image_file_name)
                frame_args.get_frame().save(full_image_path, drawing.imaging.ImageFormat.png)

    def run_ffmpeg(self):
        file_mask = os.path.join(self.temp_folder_path, self._IMAGE_FILE_TEMPLATE)
        cmd_line = ["ffmpeg", "-loglevel", "warning", "-framerate", str(self.fps), "-i", file_mask, "-y", "-c:v", "libx264", "-pix_fmt", "yuv420p", self.out_video_path]
        print(" ".join(cmd_line))
        try:
            process = subprocess.Popen(cmd_line)
            process.wait()
            exit_code = process.returncode
            
            if exit_code != 0:
                raise Exception("FFmpeg failed with exit code %d" % exit_code)
        except FileNotFoundError:
            print("Error: ffmpeg not found")


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description="Pptx2VideoConverter command line")
    parser.add_argument('--input', '-i', type=str, help="Path to presentation", default="templates/presentation.pptx")
    parser.add_argument('--output', '-o', type=str, help="Output file path", default="out/video.mp4")
    parser.add_argument('--fps', '-f', type=int, help="Frames per second", default=30)
    return parser.parse_args()


def main():
    try:
        arguments = parse_command_line_arguments()
        with slides.Presentation(arguments.input) as presentation:
            converter = Pptx2VideoConverter(presentation, arguments.output, "generated_frames", arguments.fps)

            print("Generating frames...")
            converter.generate_frames()
            print("Running FFmpeg to convert image sequence to video...")
            converter.run_ffmpeg()
            print("Done")
    except Exception as ex:
        print("Exception occurred:")
        print(str(ex))


if __name__ == "__main__":
    main()
else:
    print("This script should not be imported!")
