import aiohttp
import asyncio
import uvicorn
from fastai import *
from fastai.vision import *
from io import BytesIO
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from pathlib import Path
import torch
from fastai.vision.all import PILImage
from fastai.learner import load_learner
import pickle
import sys
import os
import firebase_admin
from firebase_admin import credentials, db
from starlette.templating import Jinja2Templates


export_file_url = 'https://drive.google.com/file/d/13LtU2BYQWuc_1-j0zhkACwJH19sa0-SR/view?usp=drive_link'
export_file_name = 'export_5cycles_model.pkl'
export_dir = Path(__file__).parent / "models"

export_dir.mkdir(parents=True, exist_ok=True)

export_file_path = export_dir / export_file_name

classes = ['Apple___Apple_scab','Apple___Black_rot','Apple___Cedar_apple_rust','Apple___healthy','Blueberry___healthy','Cherry_(including_sour)___Powdery_mildew','Cherry_(including_sour)___healthy','Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot','Corn_(maize)___Common_rust_','Corn_(maize)___Northern_Leaf_Blight','Corn_(maize)___healthy','Grape___Black_rot','Grape___Esca_(Black_Measles)','Grape___Leaf_blight_(Isariopsis_Leaf_Spot)','Grape___healthy','Orange___Haunglongbing_(Citrus_greening)','Peach___Bacterial_spot','Peach___healthy','Pepper,_bell___Bacterial_spot','Pepper,_bell___healthy','Potato___Early_blight','Potato___Late_blight','Potato___healthy','Raspberry___healthy','Soybean___healthy','Squash___Powdery_mildew','Strawberry___Leaf_scorch','Strawberry___healthy','Tomato___Bacterial_spot','Tomato___Early_blight','Tomato___Late_blight','Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot','Tomato___Spider_mites Two-spotted_spider_mite','Tomato___Target_Spot','Tomato___Tomato_Yellow_Leaf_Curl_Virus','Tomato___Tomato_mosaic_virus','Tomato___healthy','background']



#firebase_key_path = os.getenv("FIREBASE_KEY_PATH", "firebase_key.json")
cred = credentials.Certificate("./db/firebase_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://plant-disease-detection-4e7c1-default-rtdb.asia-southeast1.firebasedatabase.app/" 
})


async def download_file(url, dest):
    if dest.exists():
        return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f:
                f.write(data)


async def setup_learner():
    await download_file(export_file_url, export_file_path)
    try:
        learn = load_learner(export_file_path)
        return learn
    except RuntimeError as e:
        if len(e.args) > 0 and 'CPU-only machine' in e.args[0]:
            print(e)
            message = "\n\nThis model was trained with an old version of fastai and will not work in a CPU environment.\n\nPlease update the fastai library in your training environment and export your model again.\n\nSee instructions for 'Returning to work' at https://course.fast.ai."
            raise RuntimeError(message)
        else:
            raise


async def init_learner():
    tasks = [setup_learner()]
    result = await asyncio.gather(*tasks)
    return result[0]

learn = asyncio.run(init_learner())

index_path = Path(__file__).parent

async def homepage(request):
    index_file = index_path / 'view' / 'index.html'
    content = index_file.read_text()  
    return HTMLResponse(content)

async def features_page(request):
    features_file = index_path / 'view' / 'features.html'
    content = features_file.read_text()
    return HTMLResponse(content)

async def about_page(request):
    about_file = index_path / 'view' / 'about.html'
    content = about_file.read_text()
    return HTMLResponse(content)

async def diseases_page(request):
    formatted = []
    for d in classes:
        name = d.replace("___", " – ").replace("_", " ")
        image_name = d + ".jpg"
        formatted.append({"raw": d, "name": name, "image": image_name})
    
    jinja = Jinja2Templates(directory=str(index_path / 'view'))
    return jinja.TemplateResponse("plants.html", {"request": request, "diseases": formatted})

app = Starlette(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=['X-Requested-With', 'Content-Type']
)

app.mount('/static', StaticFiles(directory='app/static'), name='static')

app.add_route('/', homepage)
app.add_route('/features', features_page)
app.add_route('/about', about_page)
app.add_route('/plants', diseases_page)

@app.route('/analyze', methods=['POST'])
async def analyze(request):
    img_data = await request.form()
    if 'file' not in img_data:
        return JSONResponse({'error': 'No file found in the request'}, status_code=400)
    img_bytes = await (img_data['file'].read())
    img = PILImage.create(BytesIO(img_bytes))
    prediction = learn.predict(img)[0]
    prediction = str(prediction).split('__')[1] if '__' in str(prediction) else str(prediction)
    cleanpred = str(prediction).replace('_', ' ').upper()
    

    return JSONResponse({'disease_name': str(cleanpred)})




@app.route('/get-remedy', methods=['POST'])
async def get_remedy(request: Request):
    data = await request.json()
    disease_name = data.get('disease_name', '').strip().upper()
    ref = db.reference(f"/remedies/{disease_name}")
    remedy_data = ref.get()
    if remedy_data:
        return JSONResponse({
            "overview": remedy_data.get("overview", "No overview available."),
            "remedy": remedy_data.get("remedy", "No remedy available.")
        })
    else:
        return JSONResponse({
            "error": "Disease not found"
        }, status_code=404)


if __name__ == '__main__':
    if 'serve' in sys.argv:
        uvicorn.run(app=app, host='0.0.0.0', port=8080, log_level="info")
