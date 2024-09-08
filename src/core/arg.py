import argparse

def parse_arg() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Multi-Person Tracking'
    )

    parser.add_argument(
        '--input_video_path',
        required=True,
        type=str
    )

    parser.add_argument(
        '--output_video_path',
        required=True,
        type=str
    )

    parser.add_argument(
        '--model_path',
        default='models/default.pt',
        type=str
    )

    parser.add_argument(
        '--confidence_threshold',
        default=0.3,
        type=float
    )

    parser.add_argument(
        '--iou_threshold',
        default=0.7,
        type=float
    )

    return parser.parse_args()
