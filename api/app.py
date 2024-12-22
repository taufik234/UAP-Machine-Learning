from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile
from typing import Union
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model

model = load_model('..\Model\model_MNV2.h5')

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



def preprocess_image(image_path: Path) -> np.ndarray:
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array



def predict_class(image_path: Path) -> Union[dict, None]:
    try:
        preprocessed_image = preprocess_image(image_path)
        prediction = model.predict(preprocessed_image)[0]
        predicted_class_index = np.argmax(prediction)
        confidence = float(prediction[predicted_class_index])
        return {
            "class": labels[predicted_class_index],
            "confidence": confidence
        }
    except Exception as e:
        print(f"Error occurred during prediction: {e}")
        return None


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        # Read image data
        image_bytes = await image.read()
        image_array = cv2.imdecode(np.fromstring(
            image_bytes, np.uint8), cv2.IMREAD_COLOR)
        image_path = Path("temp_image.jpg")  # Temporary file for processing
        cv2.imwrite(str(image_path), image_array)

        # Predict class and confidence
        prediction_result = predict_class(image_path)

        # Remove temporary image
        image_path.unlink()

        if prediction_result:
            return JSONResponse(prediction_result)
        else:
            return JSONResponse({"error": "Error occurred during prediction"}, status_code=400)
    except Exception as e:
        print(f"Error processing image: {e}")
        return JSONResponse({"error": "Internal server error"}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
