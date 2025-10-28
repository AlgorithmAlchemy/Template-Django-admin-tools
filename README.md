# Django Template

A ready-to-use modular Django project template with a preconfigured admin panel, scalable structure, and basic HTML templates.

## Features

* Clean, modular structure
* Basic customization of Django Admin
* Template support (`templates/`)
* Ready-made examples of URL routes
* Easy integration of new applications
* Standard directories: `core/`, `apps/`, `config/`, `templates/`, `static/`

## Project Structure

```
django-template/
│
├── config/            # Project configuration (settings, urls, wsgi)
├── core/              # Core logic (middleware, mixins, utils)
├── apps/              # Modular Django applications
├── templates/         # HTML templates (including admin)
├── static/            # CSS, JS, images
├── manage.py
└── requirements.txt
```

---

# Django Custom Admin Dashboard

A Django project with a custom admin panel and theming using `admin_tools`.

## Description

This project demonstrates how to create and connect a custom template for the Django admin panel using `admin_tools` and your own templates.

## Installation

1.

```bash
git clone <repository_URL>
cd <project_name>
```

2.

```bash
pip install -r requirements.txt
```

3.

```bash
python manage.py migrate
```

4.

```bash
python manage.py runserver
```

## Usage

* Open the admin panel at `http://127.0.0.1:8000/admin/`
* The custom dashboard will replace the default one.

## Features

* Uses `admin_tools` for admin customization
* Custom templates extending the default Django templates
* Configuration and setup instructions are provided in the project documentation
