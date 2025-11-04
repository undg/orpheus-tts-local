#!/usr/bin/env python3

"""
Simple example of using Orpheus TTS as a library.
This script demonstrates how to generate speech and save it to a file.
"""

from gguf_orpheus import AVAILABLE_VOICES, generate_speech_from_api

MAX_TOKENS=4800
VOICE="tara" # dan, tara, mia, leah, jess, leo,  zac, zoe
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


def split_into_chunks(text, target_words=50):
    """Split text into chunks by sentences, aiming for target_words per chunk."""
    sentences = text.split('.')
    chunks = []
    current_chunk = []
    current_words = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        words = len(sentence.split())
        if current_words + words > target_words and current_chunk:
            chunks.append('. '.join(current_chunk) + '.')
            current_chunk = [sentence]
            current_words = words
        else:
            current_chunk.append(sentence)
            current_words += words
    
    if current_chunk:
        chunks.append('. '.join(current_chunk) + '.')
    
    return chunks


def main():
    import argparse
    import subprocess
    import os
    from pathlib import Path
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Text file to read")
    parser.add_argument("--out", default="output.wav", help="Output file")
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
            chunks = split_into_chunks(text)
            chunk_files = []
            
            for i, chunk in enumerate(chunks):
                output_path = Path(args.out)
                f_path = str(output_path.parent)
                f_name = output_path.stem
                f_ext = output_path.suffix[1:] or 'wav'  # [1:] removes dot
                f_output = f'{f_path}/{f_name}.{f_ext}'

                chunk_file = f'{f_path}/{f_name}/{f_name}_chunk{i:03d}.{f_ext}'
                chunk_files.append(chunk_file)
                print(f"\nchunk: {i+1}/{len(chunks)}")
                text_to_speech(chunk, output_file=chunk_file)
            
            # Merge with ffmpeg
            print(f"\nMerging {len(chunk_files)} chunks...")
            list_file = "/tmp/concat_list.txt"
            with open(list_file, 'w') as f:
                for cf in chunk_files:
                    f.write(f"file '{os.path.abspath(cf)}'\n")
            
            subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', list_file, '-c', 'copy', f_output], check=True)
            os.remove(list_file)
            print(f"Merged to {args.out}")
    else:
        print("provide --file input.txt")


if __name__ == "__main__":
    main()
