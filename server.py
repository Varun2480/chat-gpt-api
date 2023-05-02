from fastapi import FastAPI
from gpt_main import GPT_ROUTER
BASE_URL = "/chatgpt"
APP = FastAPI(title="GPT endpoint",
              docs_url=BASE_URL+"/apidocs",
              redoc_url=BASE_URL+"/redoc")


APP.include_router(GPT_ROUTER)