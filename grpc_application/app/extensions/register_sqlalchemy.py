from sqlalchemy import create_engine

from grpc_application.config.db_config import LocalDBConfig


def register_sqlalchemy():
    engine = create_engine(map_path(
        LocalDBConfig.db_type,
        LocalDBConfig.id,
        LocalDBConfig.password,
        LocalDBConfig.host,
        LocalDBConfig.db
    ))

    return engine

def map_path(_type, id, password, host, db, *options):

    path = _type+"://"+id+":"+password+"@"+host+"/"+db+"?"

    for option in options:
        path = path + option + "&"
    
    return path

