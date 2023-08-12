from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import csv
from pathlib import Path
import json
import data_set
from data.apt_data import router as apt_data_router

app=FastAPI()

# CORS Error Path Setting
origins = [
    "http://localhost",  # 실제 도메인으로 변경하거나 필요한 출처를 추가
    "http://localhost:3000",  # 예시 출처
]

# CORS Error Setting
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router Setting
app.include_router(apt_data_router, prefix='/apt', tags=['apt data'])

# CSV File Path Setting
bus_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/bus.csv')
d_center_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/d_center.csv')
edu_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/educational.csv')
eschool_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/eschool.csv')
kinder_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/kindergarden.csv')
mart_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/mart.csv')
road_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/road.csv')
train_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/train.csv')
hospital_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/hospital.csv')
pharmacy_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/pharmacy.csv')
admin_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/admin.csv')

# 메인페이지 접속시 html 파일 전송
from fastapi.responses import FileResponse

# DB 입출력 기능 가능

# @app.get("/")
# def call_data():
#     return 'data'


@app.get("/")
def call_data():
    return FileResponse('index.html')

@app.get("/data")
def call_back_data():
    return  {'data1':1234}

# 아파트 데이터 호출
# @app.get("/apt")
# async def call_back_data():
#     data=data_set.read_apt(apt_path)
#     return data

@app.get("/bus")
async def call_back_data():
    data=data_set.read_apt(bus_path)
    return data

@app.get("/d_center")
async def call_back_data():
    data=data_set.read_apt(d_center_path)
    return data

@app.get("/edu")
async def call_back_data():
    data=data_set.read_apt(edu_path)
    return data

@app.get("/eschool")
async def call_back_data():
    data=data_set.read_apt(eschool_path)
    return data

@app.get("/kinder")
async def call_back_data():
    data=data_set.read_apt(kinder_path)
    return data

@app.get("/mart")
async def call_back_data():
    data=data_set.read_apt(mart_path)
    return data

@app.get("/road")
async def call_back_data():
    data=data_set.read_apt(road_path)
    return data

@app.get("/train")
async def call_back_data():
    data=data_set.read_apt(train_path)
    return data

@app.get("/hospital")
async def call_back_data():
    data=data_set.read_apt(hospital_path)
    return data

@app.get("/pharmacy")
async def call_back_data():
    data=data_set.read_apt(pharmacy_path)
    return data

@app.get("/admin")
async def call_back_data():
    data=data_set.read_apt(admin_path)
    return data

# 데이터 받을거면 모델 class 생성 필수
from pydantic import BaseModel
class Data_Model(BaseModel):
    name : str
    x : float
    y : float

@app.post("/send")
def send_data(data : Data_Model):
    print(data)
    return "data send success"

# async/await 키워드로 비동기처리기능 사용
# @app.get("/data")
# async def call_back_data():
#     await (data call 함수 불러오기)
#     return  {'data1':1234}