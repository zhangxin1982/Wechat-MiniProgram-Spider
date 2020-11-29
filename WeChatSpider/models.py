from sqlalchemy import String, Column, Integer ,DATETIME ,DECIMAL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://user:pwd@host/database')
Session = sessionmaker(bind=engine)
session = None
Base = declarative_base()

class XSYX(Base):
    __tablename__ = "tb_xsyx"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    appClass = Column(Integer,nullable=False)
    time = Column(DATETIME, nullable=False)
    cityCode = Column(Integer,nullable=False)
    cityName = Column(String(200), nullable=False)

    classNumber = Column(String(100), nullable=False)
    className = Column(String(200), nullable=False)
    subclassNumber = Column(String(100), nullable=False)
    subclassName = Column(String(200), nullable=False)

    goodNumber = Column(String(50), nullable=False)
    goodTitle = Column(String(100), nullable=False)
    imageUrl = Column(String(300), nullable=False)

    price = Column(DECIMAL(20), nullable=False)
    linePrice = Column(DECIMAL(300), nullable=False)

    surplusCount = Column(Integer, nullable=False)
    restrictionBuyCout = Column(Integer, nullable=False)
    canSaleCount = Column(Integer, nullable=False)
    canSaleCycle = Column(Integer, nullable=False)
    daySalesCount = Column(Integer, nullable=False)

    monthSalesCount = Column(Integer, nullable=False)
    sumSalesCount = Column(Integer, nullable=False)
    popularityValues = Column(Integer, nullable=False)
    provinceCode = Column(Integer, nullable=False)
    areaCode = Column(Integer, nullable=False)
    skuCode = Column(String(50), nullable=False)


class SHT(Base):
    __tablename__ = "tb_sht"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    appClass = Column(Integer,nullable=False)
    time = Column(DATETIME, nullable=False)
    cityCode = Column(Integer,nullable=False)
    cityName = Column(String(200), nullable=False)

    classNumber = Column(String(100), nullable=False)
    className = Column(String(200), nullable=False)
    subclassNumber = Column(String(100), nullable=False)
    subclassName = Column(String(200), nullable=False)

    goodNumber = Column(String(50), nullable=False)
    goodTitle = Column(String(100), nullable=False)
    imageUrl = Column(String(300), nullable=False)

    price = Column(DECIMAL(20), nullable=False)
    linePrice = Column(DECIMAL(300), nullable=False)

    surplusCount = Column(Integer, nullable=False)
    restrictionBuyCout = Column(Integer, nullable=False)
    canSaleCount = Column(Integer, nullable=False)
    canSaleCycle = Column(Integer, nullable=False)
    daySalesCount = Column(Integer, nullable=False)

    monthSalesCount = Column(Integer, nullable=False)
    sumSalesCount = Column(Integer, nullable=False)
    popularityValues = Column(Integer, nullable=False)
    provinceCode = Column(Integer, nullable=False)
    areaCode = Column(Integer, nullable=False)
    skuCode = Column(String(50), nullable=False)


class DDMC(Base):
    __tablename__ = "tb_ddmc"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    appClass = Column(Integer,nullable=False)
    time = Column(DATETIME, nullable=False)
    cityCode = Column(Integer,nullable=False)
    cityName = Column(String(200), nullable=False)

    classNumber = Column(String(100), nullable=False)
    className = Column(String(200), nullable=False)
    subclassNumber = Column(String(100), nullable=False)
    subclassName = Column(String(200), nullable=False)

    goodNumber = Column(String(50), nullable=False)
    goodTitle = Column(String(100), nullable=False)
    imageUrl = Column(String(300), nullable=False)

    price = Column(DECIMAL(20), nullable=False)
    linePrice = Column(DECIMAL(300), nullable=False)

    surplusCount = Column(Integer, nullable=False)
    restrictionBuyCout = Column(Integer, nullable=False)
    canSaleCount = Column(Integer, nullable=False)
    canSaleCycle = Column(Integer, nullable=False)
    daySalesCount = Column(Integer, nullable=False)

    monthSalesCount = Column(Integer, nullable=False)
    sumSalesCount = Column(Integer, nullable=False)
    popularityValues = Column(Integer, nullable=False)
    provinceCode = Column(Integer, nullable=False)
    areaCode = Column(Integer, nullable=False)
    skuCode = Column(String(50), nullable=False)

class MTYX(Base):
    __tablename__ = "tb_mtyx"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    appClass = Column(Integer,nullable=False)
    time = Column(DATETIME, nullable=False)
    cityCode = Column(Integer,nullable=False)
    cityName = Column(String(200), nullable=False)

    classNumber = Column(String(100), nullable=False)
    className = Column(String(200), nullable=False)
    subclassNumber = Column(String(100), nullable=False)
    subclassName = Column(String(200), nullable=False)

    goodNumber = Column(String(50), nullable=False)
    goodTitle = Column(String(100), nullable=False)
    imageUrl = Column(String(300), nullable=False)

    price = Column(DECIMAL(20), nullable=False)
    linePrice = Column(DECIMAL(300), nullable=False)

    surplusCount = Column(Integer, nullable=False)
    restrictionBuyCout = Column(Integer, nullable=False)
    canSaleCount = Column(Integer, nullable=False)
    canSaleCycle = Column(Integer, nullable=False)
    daySalesCount = Column(Integer, nullable=False)

    monthSalesCount = Column(Integer, nullable=False)
    sumSalesCount = Column(Integer, nullable=False)
    popularityValues = Column(Integer, nullable=False)
    provinceCode = Column(Integer, nullable=False)
    areaCode = Column(Integer, nullable=False)
    skuCode = Column(String(50), nullable=False)

class CXYX(Base):
    __tablename__ = "tb_cxyx"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    appClass = Column(Integer,nullable=False)
    time = Column(DATETIME, nullable=False)
    cityCode = Column(Integer,nullable=False)
    cityName = Column(String(200), nullable=False)

    classNumber = Column(String(100), nullable=False)
    className = Column(String(200), nullable=False)
    subclassNumber = Column(String(100), nullable=False)
    subclassName = Column(String(200), nullable=False)

    goodNumber = Column(String(50), nullable=False)
    goodTitle = Column(String(100), nullable=False)
    imageUrl = Column(String(300), nullable=False)

    price = Column(DECIMAL(20), nullable=False)
    linePrice = Column(DECIMAL(300), nullable=False)

    surplusCount = Column(Integer, nullable=False)
    restrictionBuyCout = Column(Integer, nullable=False)
    canSaleCount = Column(Integer, nullable=False)
    canSaleCycle = Column(Integer, nullable=False)
    daySalesCount = Column(Integer, nullable=False)

    monthSalesCount = Column(Integer, nullable=False)
    sumSalesCount = Column(Integer, nullable=False)
    popularityValues = Column(Integer, nullable=False)
    provinceCode = Column(Integer, nullable=False)
    areaCode = Column(Integer, nullable=False)
    skuCode = Column(String(50), nullable=False)



