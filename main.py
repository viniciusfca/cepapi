import requests
from fastapi import FastAPI
from cachetools import TTLCache

app = FastAPI()
cache = TTLCache(maxsize=100, ttl=300)

@app.get("/cep/{cep}")
async def get_address(cep: str):
    if cep in cache:
        return cache[cep]
    else:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        address_data = response.json()
        cache[cep] = address_data
        return address_data
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, log_level="info")