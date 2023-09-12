import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import time

# Streamlit app title


st.title("Generate Images using Stable Diffusion")

model_type = st.selectbox("Select Model Type", ["Stable-Diffusion-1.5", "Anime", "Cyberpunk"])

# Text input for user to enter the text
text_input = st.text_input("Enter the text:")

# Function to send a request to the API and get the image
def get_image_from_api(text, model_type):
    # Replace with your API function call
    import requests

    d = {
        "Stable-Diffusion-1.5": "jayavibhav/trial-jv",
        "Anime": "jayavibhav/anime-dreamlike",
        "Cyberpunk": "jayavibhav/cyberpunk-style-new"
    }

    model_type = d[model_type]
    API_URL = "https://api-inference.huggingface.co/models/{}".format(model_type)
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    image_bytes = query({
        "inputs": "{}".format(text),
    })

    return image_bytes
# Check if the user has entered text
def main():
    if st.button("Generate Image"):
        if text_input:
            progress_bar = st.progress(0)
            time.sleep(0.5)
            with st.empty():
                for i in range(86):
                    progress_bar.progress(i)
                    # st.text(f"Progress: {i}%")
                    time.sleep(0.05)
            # Send a request to the API and get the image bytes
            image_bytes = get_image_from_api(text_input, model_type)
            
            progress_bar.progress(100)
        

            
            # Display the image if available
            if image_bytes:
                image = Image.open(BytesIO(image_bytes))
                st.image(image, caption="Generated Image", use_column_width=True)
            else:
                st.warning("No image received from the API.")
        else:
            st.error("Error generating image, try again in 30 seconds")

if __name__ == "__main__":
    main()
