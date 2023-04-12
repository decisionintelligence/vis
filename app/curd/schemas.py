from pydantic import BaseModel
from typing import List,Union,Dict

class DataSource(BaseModel):
    datasourceid: int
    config: dict

    class Config:
        orm_mode = True

class Chart(BaseModel):
    chartid: int
    config: dict

    class Config:
        orm_mode = True


class Dashboard(BaseModel):
    dashboardid: int
    config: dict

    class Config:
        orm_mode = True

class Dataset(BaseModel):
    datasetid: int
    query: str
    example_row: Union[Dict,None]
    config: Union[Dict,None]
    dataset_name: str

    class Config:
        orm_mode = True

class ChartTemplate(BaseModel):
    cid: int
    chart_name: str
    config: dict

    class Config:
        orm_mode = True

class Bootstrap(BaseModel):
    datasource: List[DataSource]
    chart: List[Chart]
    dashboard: List[Dashboard]
    dataset: List[Dataset]
    chart_template: List[ChartTemplate]

    class Config:
        orm_mode = True

class DataSourceConfig:
    def __init__(self,config:dict):
        print(config)
        self.host = config['host']
        self.port = config['port'] 
        self.user = config['user']
        self.password = config['password']
        self.type = config['type'] 
        self.database = config['database']
        self.table = config.get('table',None)
        self.query = config.get('query',None)


class DataSetConfig:
    def __init__(self,config:Union[dict,None],
                 dataset_name:str,
                 query:str,example_row: Union [Dict , None]):
        self.config = config
        self.query = query
        self.example_row = example_row
        self.dataset_name = dataset_name