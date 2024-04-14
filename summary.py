import av
import numpy as np
import torch
from transformers import AutoImageProcessor, AutoTokenizer, VisionEncoderDecoderModel
import store_frames
import requests
device = "cuda" if torch.cuda.is_available() else "cpu"
# store_frames.check()
# load pretrained processor, tokenizer, and model
image_processor = AutoImageProcessor.from_pretrained("./videomae-base")
tokenizer = AutoTokenizer.from_pretrained("./natural_language_generate")
model = VisionEncoderDecoderModel.from_pretrained("./DLSG_Trained_Model").to(device)

# load video
video_path = "./realtimevideos/r_demo16.mp4"      #demo2works#r_demo6works#r_demo7works#r_demo13works#r_demo16
container = av.open(video_path)

# extract evenly spaced frames from video
seg_len = container.streams.video[0].frames
clip_len = model.config.encoder.num_frames
indices = set(np.linspace(0, seg_len, num=clip_len, endpoint=False).astype(np.int64))
frames = []
container.seek(0)
for i, frame in enumerate(container.decode(video=0)):
    if i in indices:
        frames.append(frame.to_ndarray(format="rgb24"))

# generate caption
gen_kwargs = {
    "min_length": 10,
    "max_length": 20,
    "num_beams": 7,
}
# store_frames.store(video_path)
pixel_values = image_processor(frames, return_tensors="pt").pixel_values.to(device)
tokens = model.generate(pixel_values, **gen_kwargs)
caption = tokenizer.batch_decode(tokens, skip_special_tokens=True)[0]
print(caption) # A man and a woman are dancing on a stage in front of a mirror.
