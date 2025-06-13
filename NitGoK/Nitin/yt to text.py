import os
import subprocess
import speech_recognition as sr

def download_audio(youtube_url, output_file="lecture_audio.mp3"):
    """Download audio from YouTube using yt-dlp."""
    try:
        print("Downloading audio...")
        command = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "-o", output_file,
            youtube_url
        ]
        subprocess.run(command, check=True)
        print(f"Audio downloaded successfully as {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error downloading audio: {e}")
        return None

def convert_audio_to_text(audio_file):
    """Transcribe audio to text using SpeechRecognition."""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            print("Processing audio for transcription...")
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            print("Transcription completed.")
            return text
    except sr.UnknownValueError:
        return "Audio not clear enough to transcribe."
    except sr.RequestError as e:
        return f"Error with the SpeechRecognition service: {e}"

if __name__ == "__main__":
    # Input: YouTube video URL
    youtube_url = input("Enter the YouTube video URL: ")
    
    # Step 1: Download audio
    audio_file = download_audio(youtube_url)
    
    if audio_file:
        # Step 2: Convert audio to text
        transcript = convert_audio_to_text(audio_file)
        
        # Step 3: Save transcription
        with open("transcription.txt", "w", encoding="utf-8") as file:
            file.write(transcript)
        print("Transcription saved as 'transcription.txt'")
