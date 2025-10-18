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
        output_file="outputs/" + output_file if output_file else None,
        temperature=0.6,
        top_p=0.95,
        repetition_penalty=1.1,
        max_tokens=100000000,
    )

    return audio_segments


long_text = """
The wind howls across the Greenland ice sheet as Dr. Sarah Chen adjusts her goggles, squinting through the swirling snow. The drilling site's temporary shelter flaps violently against its supports, but the core extraction equipment remains steady, anchored deep into the ancient ice.
    """

voices = [
    "tara",
    "leah",
    "jess",
    "leo",
    "dan",
    "mia",
    "zac",
    "zoe",
]


def test_all_voices():
    for voice in voices:
        text_to_speech(
            "Hello, I'm "
            + voice
            + ". This is an example of using Orpheus TTS as a library.",
            voice=voice,
            output_file="example_" + voice + ".wav",
        )
        pass


def long_example_test():
    voice = "tara"
    text_to_speech(
        "Hello, I'm "
        + voice
        + ". This is an example of using Orpheus TTS as a library."
        + long_text,
        voice=voice,
        output_file="example_frost-protocol.wav",
    )


def main():
    # Example 1: Generate speech with Tara voice
    text_to_speech(
        "Hello, I'm Tara. This is an example of using Orpheus TTS as a library.",
        voice="tara",
        output_file="example_tara.wav",
    )

    # Example 2: Generate speech with a different voice
    text_to_speech(
        "Hi there, I'm Leo. I have a different voice than Tara.",
        voice="leo",
        output_file="example_leo.wav",
    )

    # test_all_voices()

    # long_example_test()

    print("All available voices:")
    for voice in AVAILABLE_VOICES:
        print(f"- {voice}")


if __name__ == "__main__":
    main()
