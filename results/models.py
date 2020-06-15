from django.db import models
from django import forms

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import desc
from config import KEY_localData

Base = declarative_base()

def createSessionSQL (keyFile):
    engineSQL = create_engine(keyFile, pool_pre_ping=True)
    Sesion = sessionmaker(bind=engineSQL)
    session = Sesion()
    return session

class pha1037(Base):
    __tablename__ = "pha1037"

    geneID = sqlalchemy.Column(String(20), primary_key=True)
    ANT0 = sqlalchemy.Column(Float)
    ANT10 = sqlalchemy.Column(Float)
    ANT20 = sqlalchemy.Column(Float)
    ANT30 = sqlalchemy.Column(Float)
    ANT45 = sqlalchemy.Column(Float)
    ANT5 = sqlalchemy.Column(Float)
    FB5 = sqlalchemy.Column(Float)
    IM = sqlalchemy.Column(Float)
    SAM = sqlalchemy.Column(Float)
    VM = sqlalchemy.Column(Float)

    def getGeneExpression(_id):
        session = createSessionSQL(KEY_localData)
        data = session.query(pha1037).filter_by(geneID=_id).all()
        session.close()
        return data[0] if len(data)>0 else None
