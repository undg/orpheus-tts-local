#!/usr/bin/env python3

"""
Simple example of using Orpheus TTS as a library.
This script demonstrates how to generate speech and save it to a file.
"""

from gguf_orpheus import AVAILABLE_VOICES, generate_speech_from_api

MAX_TOKENS=150000
VOICE="dan" # dan, tara, mia, leah, jess, leo,  zac, zoe
TEMPERATURE=0.6
TOP_P=0.95


def text_to_speech(text, output_file=None):
    """
    Convert text to speech using Orpheus TTS.

    Args:
        text (str): The text to convert to speech
        voice (str): The voice to use (default: tara)
        output_file (str): Path to save the audio file (default: None)

    Returns:
        list: Audio segments
    """
    print(f"Converting: '{text}' with voice={VOICE}, max_tokens={MAX_TOKENS} , temperature={TEMPERATURE}, top_p={TOP_P}")

    # Generate speech
    audio_segments = generate_speech_from_api(
        prompt=text,
        voice=VOICE,
        output_file=output_file,
        temperature=TEMPERATURE,
        top_p=TOP_P,
        repetition_penalty=1.1,
        max_tokens=MAX_TOKENS,
    )

    return audio_segments



def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Text file to read")
    parser.add_argument("--output", default="output.wav", help="Output file")
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
            text_to_speech(text, output_file=args.output)
    else:
        print("provide --output filename.wav")


if __name__ == "__main__":
    main()
