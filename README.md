The Plant Disease Detection System is an AI-powered application designed to identify plant diseases from leaf images and provide appropriate remedies. 
It uses a deep learning model trained with FastAI to classify diseases across various crops. 
The backend is built with FastAPI, serving the trained model for real-time predictions. Additionally, a Node.js server handles remedy suggestions based on the predicted disease, offering targeted treatments or preventive measures.

Users can upload images of affected plant leaves through a web interface. The image is processed by the backend model, which returns the disease class. 
The system then fetches corresponding remedies via a POST request from the Node.js server and displays them to the user. This tool helps farmers, gardeners, and agricultural experts quickly identify issues and take timely action, promoting healthier crops and reducing losses.

