"""
CLI for acquiring data using Obbec camera
"""

import os
import click
from orbbec_acquire.util import start_recording

orig_init = click.core.Option.__init__


def new_init(self, *args, **kwargs):
    orig_init(self, *args, **kwargs)
    self.show_default = True


click.core.Option.__init__ = new_init


@click.version_option()
@click.command(help="start recording depth and IR video")
@click.argument("base-dir", type=click.Path(), default=os.getcwd())
@click.option("--subject-name", help="subject name of the recording")
@click.option("--session-name", help="session name of the recording")
@click.option("--recording-length", "-t", type=float, default=30, help="recording time (minutes)")
@click.option("--save-ir", default=True, type=bool, help="save infrared stream")
@click.option("--preview", default=True, type=bool, help="show frame preview during recording")
@click.option("--display-time", default=True, type=bool, help="show time during the recording")
@click.option("--depth-height-threshold", default=150, type=int, help="Set the max height value for visualization only")
@click.option("--frame-rate", "-r", type=int, default=30, help="frame rate of the recording")
def record(
    base_dir,
    subject_name,
    session_name,
    save_ir,
    recording_length,
    preview,
    display_time,
    depth_height_threshold,
    frame_rate,
):
    # make base_dir if it doesn't exist
    os.makedirs(base_dir, exist_ok=True)
    # change recording time from minutes to seconds
    recording_length = recording_length * 60

    # prompt user to input session metadata
    if subject_name is None:
        subject_name = input("Input subject name: ")
    if session_name is None:
        session_name = input("Input session name: ")

    start_recording(
        base_dir=base_dir,
        subject_name=subject_name,
        session_name=session_name,
        recording_length=recording_length,
        save_ir=save_ir,
        display_frames=preview,
        display_time=display_time,
        depth_height_threshold=depth_height_threshold,
        frame_rate=frame_rate,
    )
