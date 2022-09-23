"""
@Time : 2022/9/19 10:26 
@Author : ls
@DES: 
"""
from config import settings
from fastapi.staticfiles import StaticFiles
from login import router as login_router
from order import router as order_router
from fastapi.openapi.docs import (get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html)

from fastapi import FastAPI

app = FastAPI(
    debug=settings.APP_DEBUG,
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    docs_url=None,
    redoc_url=None
)
app.include_router(login_router)
app.include_router(order_router)
app.mount('/static', StaticFiles(directory=settings.STATIC_DIR), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/swagger/redoc.standalone.js",
    )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app",
                host='127.0.0.1',
                port=8000,
                workers=2,
                reload=True)
