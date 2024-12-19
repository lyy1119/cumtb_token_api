from fastapi import FastAPI, Depends, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import aioredis
import os
from contextlib import asynccontextmanager
from getXIdToken import get_x_id_token


limitTimes = 10
redisLink = "redis://localhost:6379"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 初始化 Redis
    redis_url = os.getenv("REDIS_URL", redisLink)
    redis = await aioredis.from_url(redis_url, encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis)

    yield  # 应用运行期间的生命周期

    # 关闭 Redis 连接
    await redis.close()

# 将 lifespan 传递给 FastAPI
app = FastAPI(lifespan=lifespan)

@app.get("/api/token", dependencies=[Depends(RateLimiter(times=limitTimes, seconds=60))])
async def process_data(id: str = Query(...), pwd: str = Query(...)):
    try:
        result = await get_x_id_token(id, pwd)
        return JSONResponse(content=result , status_code=200)
    except Exception as e:
        return JSONResponse(content={"state":0 ,"error": str(e)}, status_code=500)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    if exc.status_code == 429:
        return JSONResponse(
            content={"state":0,"error": "Too many requests, please try again later."},
            status_code=429
        )
    return JSONResponse(
        content={"state":0,"error": exc.detail},
        status_code=exc.status_code,
    )
