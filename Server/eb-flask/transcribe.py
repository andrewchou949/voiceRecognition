import whisper
import tempfile
import openai
# from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("OPENAI_API_KEY")


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
    openai.api_key = password
    try:
        stream = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Summarize the following text."},
                    {"role": "user", "content": prompt}],
            stream=True
        )
        response = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content if chunk.choices[0].delta else None
            if content:
                response += content
        return response.strip()
        # Does not work openai >= 1.0.0
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[{"role": "system", "content": "Summarize the following text."},
        #             {"role": "user", "content": prompt}]
        # )
        # return response.choices[0].message['content'].strip()
        # # work with newer version of openai (>= 1.0.0)
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt="Summarize the following text: {}".format(prompt),
        #     temperature=0.7,
        #     max_tokens=150,
        #     top_p=1.0,
        #     frequency_penalty=0.0,
        #     presence_penalty=0.0
        # )
        # return response.choices[0].text.strip()
        # 0.28 openai
        # response = openai.Completion.create(
        #     engine="davinci",  # Adjust as needed based on available models in 0.28
        #     prompt=f"Summarize the following text: {prompt}",
        #     max_tokens=150,
        #     n=1,
        #     stop=None,
        #     temperature=0.5
        # )
        # # return response.choices[0].text.strip()
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "system", "content": "Your task is to summarize the following text."},
        #         {"role": "user", "content": prompt}
        #     ]
        # )
        # # Assuming the response format is similar to Completion and ChatCompletion
        # return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error in generate_summary: {e}")
        return None