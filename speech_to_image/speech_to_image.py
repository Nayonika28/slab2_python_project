import speech_recognition as sr
import requests
from PIL import Image
from io import BytesIO

# Step 1: Voice to Text
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("🎤 Speak your image prompt...")
    audio = recognizer.listen(source)

try:
    prompt = recognizer.recognize_google(audio)
    print(f"📝 You said: {prompt}")
except:
    print("❌ Could not recognize your voice")
    exit()

# Step 2: Hugging Face API (Stable Diffusion v1-4)
API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {
    "Authorization": "Bearer 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"
}
response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

# Step 3: Check if image was returned
if response.headers["content-type"] == "image/png":
    image = Image.open(BytesIO(response.content))
    image.show()
    image.save("generated_image.png")
    print("✅ Image saved as 'generated_image.png'")
else:
    print("❌ Failed to generate image.")
    print("📩 Server response:", response.text)
