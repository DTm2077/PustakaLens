import requests
import os
import time

API_URL = "http://127.0.0.1:8000/scan_predict"
# Use a placeholder image path (MUST EXIST)
TEST_IMAGE_PATH = "ml_backend\dataset\Peksi_batik\img1.jpg" 

def test_prediction():
    print("\n--- FINAL TEST: BYPASSING CHROME ---")
    
    if not os.path.exists(TEST_IMAGE_PATH):
        print(f"❌ Error: Image not found at {TEST_IMAGE_PATH}. Please update path.")
        return

    print(f"🚀 Sending image: {TEST_IMAGE_PATH} to Python API...")

    try:
        # Send the image file using the client's network stack
        with open(TEST_IMAGE_PATH, "rb") as img_file:
            files = {"image": img_file} 
            response = requests.post(API_URL, files=files, timeout=10) # Added timeout

        # Check the Response Status and Content
        if response.status_code == 200:
            data = response.json()
            
            print("\n✅ SUCCESS: BACKEND IS PERFECT.")
            print("========================================")
            print(f"AI Prediction:  {data['motif']}")
            print(f"Confidence:     {data['confidence']:.2f}%")
            print("-" * 40)
            print("ACTION REQUIRED: Connect a real phone or deploy the API.")
            print("========================================")
        
        else:
            print(f"\n❌ BACKEND FAILED (Status {response.status_code})")
            print("Check Python terminal for error trace.")

    except requests.exceptions.ConnectionError:
        print("\n❌ CONNECTION FAILED: Uvicorn not listening or port blocked.")
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")

if __name__ == "__main__":
    test_prediction()