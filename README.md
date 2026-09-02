## Project structure

```text
flask-form-lab/
├── app.py
├── templates/
│   ├── base.html
│   └── contact.html
└── static/
    └── style.css
```

## What the project demonstrates

Students practise:

* Flask routes with **GET and POST**
* Reading form data using `request.form`
* **Manual validation**
* Displaying validation errors in the template
* Using **flash messages**
* Template inheritance with `base.html`
* Basic **Bootstrap styling**
* Redirecting after successful submission

## How to build it (including on Render.com)
```bash
uv sync
```

## How to run it in development mode

```bash
uv run app.py
```

## How to run it in production (e.g. on Render.com)
```bash
uv run gunicorn app:app
```

Then open:

```
http://127.0.0.1:8000/contact
```
