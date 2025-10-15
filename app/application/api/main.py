from fastapi import FastAPI


def create_app():
    app = FastAPI(
        title="Simple Kafka Chat",
        description="Simple Kafka Chat",
        docs_url="/api/docs",
        debug=True,
    )
    return app
