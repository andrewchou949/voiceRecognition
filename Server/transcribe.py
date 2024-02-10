import whisper
import tempfile

def transcribe_audio(audio_stream):
    """
    Transcribes an audio stream using OpenAI's Whisper model.

    Parameters:
    - audio_stream: An audio file stream.

    Returns:
    - Transcribed text as a string.
    """
    model = whisper.load_model("base")  # You can choose a different model size as needed

    # Use a temporary file to save the audio stream
    with tempfile.NamedTemporaryFile(suffix=".mp3") as tmp_audio_file:
        tmp_audio_file.write(audio_stream.read())
        tmp_audio_file.seek(0)  # Go back to the beginning of the file

        # Transcribe the audio
        result = model.transcribe(tmp_audio_file.name)
        
    return result["text"]
