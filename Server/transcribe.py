import whisper
import tempfile
import openai

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

# using openai turbo API to generate text
# make sure to update interface to 1.0.0 (openai migrate)
def generate_summary(prompt):
    openai.api_key = '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'
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Summarize the following text."},
                    {"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error in generate_summary: {e}")
        return None