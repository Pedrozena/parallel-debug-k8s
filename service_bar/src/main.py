from fastapi import FastAPI, Response, status, Request
import uvicorn
import asyncio
import uvicorn
import urllib.request
import logging

logger = logging.getLogger("uvicorn.error")

RETRY = 10


async def appDefinition():
    '''
    Definition of FastAPI app object and its route handlers.
    '''
    tags_metadata = [
        {
            "name": "test",
            "description": "test",
        },
    ]
    app = FastAPI(
        title="bar",
        description="HTTP server for testing cloud code debug capability",
        version="0.1.0",
        openapi_tags=tags_metadata,
        swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png", 
    )

    @app.get("/test/", tags=["test"], responses={
        200: {"content": {"application/json": {}}},
    })
    async def test(response: Response):
        '''
        test method
        '''
        return True

    @app.get("/")
    def read_root(request: Request):
        '''
        \f
        Root Handler
        '''
        return {"Description": "bar microservice. visit "+str(request.base_url)+"docs/ for documentation"}

    return app

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(appDefinition())

    uvicorn.run(app, host="0.0.0.0", port=8082, log_level="info")