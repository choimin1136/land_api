from fastapi import APIRouter
from .type.apt_data_type import AptData
from data_set import read_apt
from pathlib import Path

router = APIRouter()

# CSV File Path Setting
# apt_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/apt_cluster.csv')
# apt_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/test_data.csv')
apt_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/df_800_all.csv')
# apt_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/df_800.csv')
# apt_path=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/dd.csv')
apt_path2=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/df_1500_all.csv')
# apt_path2=Path('/Users/hyeok/Desktop/Development/Python/ai_project/land_api/data_table/df_1500.csv')

@router.get("/")
async def call_back_data():
    data=read_apt(apt_path)
    return data
@router.get("/2")
async def call_back_data():
    data=read_apt(apt_path2)
    return data

@router.post("/{name}")
async def apt_data(name: str,data: AptData):
    return {"message": f"Received custom data for {name} : {data}"}
