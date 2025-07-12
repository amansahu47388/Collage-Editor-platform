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
   git clone <repository-url>
   cd collage_editor
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv env
   env\Scripts\activate  # Windows
   source env/bin/activate  # macOS/Linux
   ```

3. **Install Dependencies**
   ```bash
   pip install django pillow
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

## 🛠️ Technical Details

### Models
- `Collage`: Stores collage metadata and grid style
- `ImageItem`: Stores individual images for each collage

### Views
- `upload_collage()`: Handle collage creation
- `collage_display()`: Display individual collages
- `collage_list()`: List all collages
- `delete_collage()`: Delete collages

### URL Patterns
```python
urlpatterns = [
    path('', views.collage_list, name='collage_list'),
    path('upload/', views.upload_collage, name='upload_collage'),
    path('collage/<int:collage_id>/', views.collage_display, name='collage_display'),
    path('collage/<int:collage_id>/delete/', views.delete_collage, name='delete_collage'),
]
```


**Made with ❤️ for creative people everywhere** 