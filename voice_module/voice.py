import os
import torch

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'voice_module/model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
                                   local_file)

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)


#aidar, baya, kseniya, xenia, eugene, random
def get_speech(text, speaker = 'xenia'):
    audio_paths = model.save_wav(text=text,
                             speaker=speaker,
                             sample_rate=24000)
    return audio_paths
