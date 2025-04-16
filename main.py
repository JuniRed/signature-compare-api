from fastapi import FastAPI, UploadFile, File
from skimage.metrics import structural_similarity as compare_ssim
import numpy as np
import cv2

app = FastAPI()

def read_image_bytes(img_bytes):
    img_np = np.frombuffer(img_bytes, np.uint8)
    return cv2.imdecode(img_np, cv2.IMREAD_GRAYSCALE)

@app.post("/compare-signatures")
async def compare_signatures(img1: UploadFile = File(...), img2: UploadFile = File(...)):
    try:
        image1 = read_image_bytes(await img11.read())
        image2 = read_image_bytes(await img22.read())

        # Resize images if necessary
        if image1.shape != image2.shape:
            image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

        score, _ = compare_ssim(image1, image2, full=True)
        return {"similarity_score": round(score, 4)}
    except Exception as e:
        return {"error": str(e)}
