create table tb_ddmc
(
    id                 int auto_increment
        primary key,
    appClass           int          null,
    time               datetime     null,
    cityCode           int          null,
    cityName           varchar(200) null,
    classNumber        varchar(100) null,
    className          varchar(200) null,
    subclassNumber     varchar(100) null,
    subclassName       varchar(200) null,
    goodNumber         varchar(50)  null,
    goodTitle          varchar(100) null,
    imageUrl           varchar(300) null,
    price              decimal(20)  null,
    linePrice          decimal(20)  null,
    surplusCount       int          null,
    restrictionBuyCout int          null,
    canSaleCount       int          null,
    canSaleCycle       int          null,
    daySalesCount      int          null,
    monthSalesCount    int          null,
    sumSalesCount      int          null,
    popularityValues   int          null,
    provinceCode       int          null,
    areaCode           int          null,
    skuCode            varchar(50)  null
);


