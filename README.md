# 🖼️ ImageLabeler — Web App for Dataset Creation

ImageLabeler is a **web application** that makes it easy to create labeled datasets for **machine learning** (e.g., TensorFlow Object Detection).  
It works with **any type of image**, and even lets users capture images directly from their **webcam** (if available).

Users can draw bounding boxes, assign labels, and export annotations in multiple formats:

- **JSON** → images are encoded in Base64 with their annotations
- **ZIP** → JPEG images + TFOD-compatible XML annotations

## 📸 Screenshot

![Screenshot](https://github.com/garywillcodeit/image-labeler/blob/main/screenshots/screenshot1.png)

## 🔧 Tech Stack

- **Frontend** → Vite.js + TypeScript

  - Responsive web interface for labeling and webcam capture

- **Backend** → Flask (Python)

  - Serves the web app and exposes REST endpoints for dataset management

- **Export formats** →

  - JSON (images as Base64 + annotations)
  - ZIP (JPEG images + TensorFlow Object Detection XML annotations)

- **Storage** → Local filesystem

  - `app/database/images_files` → stores image files
  - `app/database/images_data` → stores annotation data (bounding boxes, labels, etc.)

- **Deployment** → Single repository (Flask serves both the API and the built Vite frontend)

## 📱 Features

- Works with **any type of image** (JPEG, PNG, etc.)
- Capture new images directly via **webcam** (if available)
- Draw **bounding boxes** on images and assign labels
- Store images and annotation data locally in the project folders
- Export datasets in multiple formats:
  - **JSON** (image as Base64 + annotations)
  - **ZIP** (JPEG image + TensorFlow Object Detection XML annotations)
- Clean and intuitive interface (built with Vite + TypeScript, served by Flask)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/garywillcodeit/image-labeler
cd image-labeler
```

### 2. Create a virtual environment (Python 3.10.12)

```
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

#### 4. Run the server

```
python run.py
```

By default, the app runs on: http://localhost:5000

### 🔧 (Optional) Frontend source

The frontend was developed with **Vite.js + TypeScript**, then built and integrated into Flask:

- `app/templates` → contains `index.html` (build output)
- `app/static` → contains JS, CSS, and assets (build output)

For simplicity, the **frontend source code is not included in this repository**.  
If you wish to view or modify the original Vite + TypeScript source, please contact me — I can grant access as a collaborator.

## 📂 Project Structure (simplified)

```
image-labeler/
├── app/
│ ├── static/ # JS, CSS, assets (Vite build output)
│ ├── templates/ # index.html (Vite build output)
│ ├── database/
│ │ ├── images_files/ # Stored image files
│ │ └── images_data/ # Stored annotations (bounding boxes, labels, etc.)
│ ├── controllers/ # Business logic for image/annotation handling
│ ├── routes/ # Flask route definitions
│ ├── utils/ # Helper functions, validators
│ └── init.py # Flask app initialization
├── config.py # App configuration (port, debug, etc.)
├── requirements.txt # Python dependencies
├── run.py # App entry point
└── LICENSE # MIT license
```

## 🧠 Notes

- This project is designed as a **local tool**:

  - Images and annotations are stored on the local filesystem (under `app/database/`).
  - No external database or cloud storage is required.

- The **frontend** was developed with Vite.js + TypeScript, then built and integrated into Flask:

  - `app/templates/` → contains the build `index.html`
  - `app/static/` → contains JS, CSS, and assets

- For simplicity, the **frontend source code is not included** in this repository.  
  If you wish to access or modify it, please contact me (access can be granted to collaborators).

- This tool is not intended for production deployment, but as a **practical utility for dataset creation**.

- Exports are provided in **two formats**:
  - JSON (with images encoded in Base64)
  - ZIP (with JPEG files + TFOD-compatible XML annotations)

## ✅ Project Status

- Stable and fully functional for local use
- Supports **any image type** + **webcam capture**
- Export works in both formats:
  - JSON (Base64 images + annotations)
  - ZIP (JPEG + TFOD-compatible XML)
- Designed as a **local utility** for dataset creation (not production deployment)
- Future updates will only address potential bug fixes

## 🔮 Future Improvements

This project is considered **feature-complete** and no further development is planned.  
However, contributions are welcome if someone wishes to extend it (new export formats, cloud integration, etc.).
