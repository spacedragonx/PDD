import firebase_admin
from firebase_admin import credentials, db


cred = credentials.Certificate("./firebase_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "url"  
})


reme = {
  "APPLE SCAB": {
    "overview": "Apple scab is a fungal disease caused by Venturia inaequalis, leading to dark, scabby lesions on leaves and fruit. It can reduce fruit quality and yield.",
    "remedy": "Use resistant varieties, apply fungicides such as captan or myclobutanil during early growth stages, and remove fallen leaves to reduce spore buildup."
  },
  "BLACK ROT": {
    "overview": "Black rot is a fungal disease caused by Botryosphaeria obtusa that affects apples, resulting in rotting fruit and dark leaf lesions.",
    "remedy": "Prune infected branches, use fungicides like thiophanate-methyl, and ensure proper air circulation through tree spacing."
  },
  "CEDAR APPLE RUST": {
    "overview": "Cedar apple rust is a fungal disease that affects apples and junipers, creating bright orange spots on apple leaves.",
    "remedy": "Remove nearby cedar trees, use resistant apple cultivars, and apply fungicides early in the season."
  },
  "POWDERY MILDEW": {
    "overview": "Powdery mildew is a fungal infection that covers leaves with a white, powdery substance, affecting photosynthesis.",
    "remedy": "Use sulfur-based fungicides, remove infected leaves, and improve airflow around plants."
  },
  "CERCOSPORA LEAF SPOT GRAY LEAF SPOT": {
    "overview": "A foliar fungal disease in corn caused by Cercospora zeae-maydis, resulting in elongated gray lesions.",
    "remedy": "Rotate crops, use resistant hybrids, and apply fungicides when disease risk is high."
  },
  "COMMON RUST": {
    "overview": "Common rust in maize is caused by Puccinia sorghi and leads to reddish-brown pustules on leaves.",
    "remedy": "Use resistant corn varieties and apply fungicides like strobilurins if infection is severe."
  },
  "NORTHERN LEAF BLIGHT": {
    "overview": "Caused by Exserohilum turcicum, this disease creates long, gray-green lesions on corn leaves.",
    "remedy": "Choose resistant hybrids, rotate crops, and apply fungicides as needed."
  },
  "BLACK ROT (GRAPE)": {
    "overview": "A common fungal disease in grapes that causes black spots on leaves and mummified fruit.",
    "remedy": "Prune infected vines, remove mummies, and spray protective fungicides in early spring."
  },
  "ESCA (BLACK MEASLES)": {
    "overview": "Esca affects mature grapevines, causing tiger-striping on leaves and dry rot in wood.",
    "remedy": "Remove infected vines, avoid pruning wounds during wet conditions, and apply protective treatments like sodium arsenite (where permitted)."
  },
  "LEAF BLIGHT (ISARIOPSIS LEAF SPOT)": {
    "overview": "A fungal grape disease marked by angular leaf spots and potential defoliation.",
    "remedy": "Practice canopy management, prune infected areas, and apply fungicides like mancozeb."
  },
  "HAUNGLOGBING (CITRUS GREENING)": {
    "overview": "A bacterial disease spread by the Asian citrus psyllid causing yellowing and misshapen fruit.",
    "remedy": "Control psyllid vectors using insecticides and remove infected trees to prevent spread."
  },
  "BACTERIAL SPOT (PEACH)": {
    "overview": "A disease affecting peaches caused by Xanthomonas campestris, leading to leaf spots and fruit lesions.",
    "remedy": "Use copper-based sprays, plant resistant varieties, and prune for better airflow."
  },
  "BACTERIAL SPOT (PEPPER)": {
    "overview": "Caused by Xanthomonas spp., it leads to dark, water-soaked lesions on pepper leaves and fruits.",
    "remedy": "Apply bactericides such as copper sprays and practice crop rotation."
  },
  "EARLY BLIGHT": {
    "overview": "A tomato and potato disease caused by Alternaria solani that causes target-like leaf spots.",
    "remedy": "Remove infected foliage, apply fungicides like chlorothalonil, and rotate crops."
  },
  "LATE BLIGHT": {
    "overview": "A devastating potato and tomato disease caused by Phytophthora infestans, leading to leaf and tuber rot.",
    "remedy": "Destroy infected plants, use resistant varieties, and apply fungicides preventatively."
  },
  "LEAF SCORCH": {
    "overview": "A fungal disease in strawberries that results in dark blotches and leaf death.",
    "remedy": "Use disease-free plants, rotate crops, and apply fungicides during early growth."
  },
  "BACTERIAL SPOT (TOMATO)": {
    "overview": "Affects tomato foliage and fruit, causing small, water-soaked spots.",
    "remedy": "Use certified seeds, copper sprays, and practice field sanitation."
  },
  "EARLY BLIGHT (TOMATO)": {
    "overview": "Characterized by brown concentric rings on tomato leaves and fruit.",
    "remedy": "Apply fungicides such as maneb and remove infected plant debris."
  },
  "LATE BLIGHT (TOMATO)": {
    "overview": "Leads to rapidly spreading lesions on tomato foliage and fruit, especially in cool, wet conditions.",
    "remedy": "Use disease-resistant varieties, apply fungicides, and destroy infected plants."
  },
  "LEAF MOLD": {
    "overview": "Caused by Passalora fulva, this disease results in yellow spots on the upper surface and mold on the underside of tomato leaves.",
    "remedy": "Ensure proper ventilation, use resistant cultivars, and apply appropriate fungicides."
  },
  "SEPTORIA LEAF SPOT": {
    "overview": "A common tomato disease producing small, round spots with dark borders and gray centers.",
    "remedy": "Remove affected leaves, rotate crops, and apply fungicides like chlorothalonil."
  },
  "SPIDER MITES TWO SPOTTED SPIDER MITE": {
    "overview": "Tiny pests that cause yellowing and stippling of tomato leaves.",
    "remedy": "Use miticides or insecticidal soap and maintain adequate humidity."
  },
  "TARGET SPOT": {
    "overview": "Fungal disease caused by Corynespora cassiicola resulting in bullseye-shaped lesions.",
    "remedy": "Apply fungicides and reduce humidity through proper spacing and pruning."
  },
  "TOMATO YELLOW LEAF CURL VIRUS": {
    "overview": "A viral disease spread by whiteflies that causes leaf curling and yellowing in tomatoes.",
    "remedy": "Use resistant varieties, control whiteflies, and remove infected plants."
  },
  "TOMATO MOSAIC VIRUS": {
    "overview": "A viral infection resulting in mottled leaves and stunted growth.",
    "remedy": "Disinfect tools, avoid tobacco use near plants, and use resistant varieties."
  }
}


ref = db.reference('remedies')


ref.set(reme)