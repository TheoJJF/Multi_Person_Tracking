# - Libraries ---------------------------------------------------------------

import cv2
import os
import supervision as sv

from collections import defaultdict, deque
from ultralytics import YOLO
from arg import parseArg

# ---------------------------------------------------------------------------

if __name__ == '__main__':
    arguments = parseArg()

    # Storing video information:
    # - Width
    # - Height
    # - Frames per second
    # - Total frames
    videoInfo = sv.VideoInfo.from_video_path(video_path=arguments.input_video_path)

    # Loads YOLOv8x model as default, or use custom model.
    model = YOLO(arguments.model_path)

    # Add multi-object tracking.
    byteTrack = sv.ByteTrack()

    # Calculate dynamic line thickness and font size based on video resolution.
    thickness = sv.calculate_optimal_line_thickness(resolution_wh=videoInfo.resolution_wh)
    fontSize = sv.calculate_optimal_text_scale(resolution_wh=videoInfo.resolution_wh)

    # Create necessary annotators.
    boxCornerAnnotators = sv.BoxCornerAnnotator(thickness=thickness)
    labelAnnotators = sv.LabelAnnotator(
        text_scale=fontSize,
        text_thickness=thickness,
        text_position=sv.Position.BOTTOM_LEFT
    )

    # Loop over all frames.
    framesGenerator = sv.get_video_frames_generator(source_path=arguments.input_video_path)

    with sv.VideoSink(target_path=arguments.output_video_path, video_info=videoInfo) as vidSink:
        for frame in framesGenerator:
            output = model(frame)[0]

            # Covert detection to supervision objects.
            detections = sv.Detections.from_ultralytics(output)

            # Disregard detection with less than 30% confidence(default).
            detections = detections[detections.confidence > arguments.confidence_threshold]

            # Run non-max suppresion with IoU(default) = 0.7.
            detections = detections.with_nms(threshold=arguments.iou_threshold)

            # Update.
            detections = byteTrack.update_with_detections(detections=detections)

            # Create tracker ID for each individual person.
            labels = [f"#{id}" for id in detections.tracker_id]

            annotatedFrame = frame.copy()

            # Annotate frames.
            annotatedFrame = boxCornerAnnotators.annotate(
                scene=annotatedFrame,
                detections=detections
            )

            annotatedFrame = labelAnnotators.annotate(
                scene=annotatedFrame,
                detections=detections,
                labels=labels
            )

            vidSink.write_frame(annotatedFrame)
        cv2.destroyAllWindows()
