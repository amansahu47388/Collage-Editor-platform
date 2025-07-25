# 🎨 Collage Editor Platform

A Django-based web application for creating beautiful image collages with multiple layout options.

## ✨ Features

- **Multiple Grid Styles**: 2x2, 3x3, 4x4, 2x3, 3x2, 4x3, 3x4
- **Seamless Layouts**: Images without gaps
- **Multiple File Upload**: Up to 10 images
- **Download Functionality**: Save as PNG
- **Delete Management**: Remove collages with confirmation
- **Responsive Design**: Works on all devices

## 🚀 Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/amansahu47388/Collage-Editor-platform.git
   cd collage_editor
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv env
   env\Scripts\activate  # Windows
   source env/bin/activate  # macOS/Linux
   ```

3. **Run requirement file**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start Server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to use the application.

## 📁 Project Structure

```
collage_editor/
├── collage_editor/          # Django settings
├── collage/                 # Main app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Form definitions
│   ├── urls.py             # URL routing
│   └── templates/          # HTML templates
├── manage.py
└── README.md
```

## 🎯 Usage

### Creating a Collage
1. Go to `/upload/`
2. Enter collage title
3. Select grid style (2x2, 3x3, etc.)
4. Upload images (max 10)
5. Click "Create Grid Collage"

### Managing Collages
- **View**: Click "View" on any collage
- **Download**: Click "Download Collage" button
- **Delete**: Click "Delete" with confirmation



**Made with ❤️ for creative people everywhere** 