# Simple Python Text-to-Speech Tool

This uses the TTS api to generate JSON data into audio files with spoken lines

## Requirements
- Python 3.10+ (TTS requires 3.8+/<3.12 and torch requires 3.10)
- pyenv 2.5.7+

## Installation
- Install pyenv with
```
brew install pyenv
```
For arm64 environments, use
```
arch -arm64 brew install pyenv --head
```

- Install python 3.10+
```
pyenv install 3.10.12
```

and set your local environment to 3.10.12 with

```
pyenv local 3.10.12
```

- Make sure you set up a virtual environment with
```
python -m venv my_env_name
source venv/bin/activate
```

For more information on python virtual environments, refer to this video:

<a href="https://youtu.be/Y21OR1OPC9A?si=Xf6J4qEucnchQz_3" target="_blank"><img src="http://img.youtube.com/vi/Y21OR1OPC9A/0.jpg" width="240" height="180" border="10" /></a>

- Install TTS by following the instructions on https://github.com/coqui-ai/TTS

  Quick jist of what you need to do is just run
  ```
  pip install TTS
  ```
  But refer to the link above if this changes
  

## Usage
- Make sure your `data.json` has a json array of objects structured like so:
```js
[
  {
    ...
    text: "Text to convert to audio"
    audio: "audio_file_name"
  }
]
```
- Run `main.py` with:
```
python main.py
```

This will output `.wav` files to the `/outputs` folder


## Options

If you want to test different models instead of the one provided by default, a list of them can be generated with the command
```
tts --list_models
```

You can then select one of the listed models and swap out the

```python
model = ...
```

in `main.py` to switch the model
(note that some of the models may not work very well, be slower, or not work at all sometimes)


## Troubleshooting

If you have any problems try refering to the [coqui repo](https://github.com/coqui-ai/TTS) listed above and/or refer to steps in this youtube video

<a href="https://youtu.be/EyzRixV8s54?si=91SdHQUhmaTdpZaC" target="_blank"><img src="http://img.youtube.com/vi/EyzRixV8s54/0.jpg" width="240" height="180" border="10" /></a>


