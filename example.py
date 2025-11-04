#!/usr/bin/env python3
"""
Simple example of using Orpheus TTS as a library.
This script demonstrates how to generate speech and save it to a file.
"""

from gguf_orpheus import AVAILABLE_VOICES, generate_speech_from_api


def text_to_speech(text, voice="tara", output_file=None):
    """
    Convert text to speech using Orpheus TTS.

    Args:
        text (str): The text to convert to speech
        voice (str): The voice to use (default: tara)
        output_file (str): Path to save the audio file (default: None)

    Returns:
        list: Audio segments
    """
    print(f"Converting: '{text}' with voice '{voice}'")

    # Generate speech
    audio_segments = generate_speech_from_api(
        prompt=text,
        voice=voice,
        output_file="example_outputs/" + output_file if output_file else None,
    )

    return audio_segments


voices = [
    # "tara",
    # "leah",
    # "jess",
    # "leo",
    # "dan",
    # "mia",
    # "zac",
    # "zoe",
    "kaya",
]


def test_all_voices():
    for voice in voices:
        text_to_speech(
            "Hello, I'm "
            + voice
            + ". This is an example of using Orpheus TTS as a library.",
            voice=voice,
            output_file=voice + ".wav",
        )
        pass


def main():
    test_all_voices()

    print("All available voices:")
    for voice in AVAILABLE_VOICES:
        print(f"- {voice}")


if __name__ == "__main__":
    main()
