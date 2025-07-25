# 🖼️ Speech-to-Image Generation using Hugging Face API 🎤

This project converts **spoken prompts** into **AI-generated images** using:
- `speech_recognition` for voice input
- Hugging Face’s `Stable Diffusion` model for image generation

---

## 🚀 Features

- 🎤 **Speech-to-Text** using Google Speech Recognition
- 🧠 **Text-to-Image** using Hugging Face’s `stable-diffusion-v1-4` model
- 🖼️ Displays & saves the generated image locally

---

## 📦 Requirements

Install the required Python libraries before running:

pip install speechrecognition requests pillow pyaudio
```

> ⚠️ You may also need to install PortAudio separately for `pyaudio` to work properly on your system.

---

## 🔑 API Key Setup

1. Create a free account on Hugging Face: https://huggingface.co
2. Go to: https://huggingface.co/settings/tokens
3. Generate a read-access token
4. Add your token to the Python file like this:

```python
headers = {
    "Authorization": "Bearer hf_your_token_here"
}
```

---

## 📂 Project Structure

```
Speech-to-Image/
│
├── speech_to_image.py         # Main Python script
├── generated_image.png        # Output image saved after speech
└── README.md                  # Project documentation
```

---

## 🧠 How It Works

1. Run the script:
 
   python speech_to_image.py
   ```

2. You will be prompted to **speak your idea**.

3. The program will:
   - Convert your voice to text using Google Speech Recognition
   - Use Hugging Face API to generate an image based on that text
   - Display and save the image as `generated_image.png`

---

## 🧪 Example Usage

```plaintext
🎤 Speak your image prompt...
📝 You said: A cat flying a spaceship
🧠 Generating image from Hugging Face...
✅ Image saved as 'generated_image.png'
```

---

## 🖼️ Output Sample

*Prompt:* `"A panda playing guitar on the moon"`  
*Output:*  

![Sample Output](generated_image.png)

---

## 🔗 Credits & Tech Used

- 🤖 Hugging Face Inference API  
- 🧠 Stable Diffusion Model (`CompVis/stable-diffusion-v1-4`)  
- 🎤 Google Speech Recognition API  
- 🐍 Python

---

## ✍️ Author

Made with ❤️ by **[Nayonika](https://github.com/Nayonika28)**  
Internship Project – Python, July 2025
