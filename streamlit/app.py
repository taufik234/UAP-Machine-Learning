import os
import streamlit as st
import numpy as np
import tensorflow as tf

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

labels = {
    0: 'Electrolytic-capacitor',
    1: 'LED',
    2: 'armature',
    3: 'attenuator',
    4: 'cartridge-fuse',
    5: 'clip-lead',
    6: 'filament',
    7: 'heat-sink',
    8: 'jumper-cable',
    9: 'limiter-clipper',
    10: 'memory-chip',
    11: 'microchip',
    12: 'microprocessor',
    13: 'potentiometer',
    14: 'pulse-generator',
    15: 'semiconductor-diode',
    16: 'solenoid',
    17: 'step-down-transformer',
}



def load_model():
    model = tf.keras.models.load_model(
        '../assets/model/model_MNV2.h5')
    return model



def predict(model, image):
    processed_image = preprocess_image(image)
    predictions = model.predict(np.expand_dims(processed_image, axis=0))
    predicted_label = np.argmax(predictions)
    confidence = np.max(predictions) * 100  
    return labels[predicted_label], confidence



def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0 
    return image



st.title("🖼️ Machine Learning Classification App")


uploaded_file = st.file_uploader(
    "📂 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    from PIL import Image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    model = load_model()
    label, confidence = predict(model, image)

    st.success(f"✅ **Predicted Label**: {label}")
    st.info(f"🔍 **Confidence Level**: {confidence:.2f}%")

    st.button("🔄 Predict Again")

st.write("\n\n👨‍💻 Developed by Taufik")
