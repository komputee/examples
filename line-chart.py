from fastapi import FastAPI
from komputee import KomputeeFunctionRequest, KomputeeFunctionResponse, LineChart, Series, BarChart

app = FastAPI()


@app.post("/my-function", response_model=KomputeeFunctionResponse)
async def myFunction(params: KomputeeFunctionRequest):
    return {
        "data": {
            "my-line": BarChart(index=[1, 2, 3], series=[
                Series(data=[1, 2.4, 3], name="series 1"),
            ])
        }
    }
