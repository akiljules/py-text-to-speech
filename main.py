import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"
output_path = "outputs/"
model = "tts_models/en/ljspeech/fast_pitch"

tts = TTS(model_name=model).to(device)

def generate_audio(text="", filename="output.wav"):
    if not text or text == "":
        return
    
    tts.tts_to_file(text=text, file_path=f"{output_path}{filename}.wav")
    return output_path + filename


def read_json_file(file_path="./data.json"):
    import json
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

data = read_json_file('./data.json')

#loop over json object
for i in range(len(data)):
    text = data[i]['text']
    filename = data[i]['audio']
    audio_path = generate_audio(text, filename)
    print(f"Generated audio file: {filename}")  