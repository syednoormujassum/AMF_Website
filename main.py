from datetime import datetime
import os

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, select_autoescape


app = FastAPI(title="NeuroKids Physio Studio")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Use a plain Jinja2 environment for template rendering to avoid
# any incompatibilities between Starlette's templating helper and
# the current Jinja2 version.
jinja_env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html", "xml"]),
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    year = datetime.now().year
    template = jinja_env.get_template("index.html")
    html = template.render(request=request, year=year)
    return HTMLResponse(content=html)


@app.post("/contact")
async def contact(
    request: Request,
    name: str = Form(...),
    phone: str = Form(...),
    email: str | None = Form(None),
    message: str | None = Form(None),
):
    # In a real app, you would save to a database or send an email.
    # For now, just redirect back to the home page with a simple UX.
    url = request.url_for("home")
    response = RedirectResponse(url=url, status_code=303)
    return response


def main() -> None:
    """Convenience entrypoint for `uv run main.py`."""
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)


if __name__ == "__main__":
    main()
