import shapefile


def shapfile_reader(path):
    
    myshp = open(path / "data" / "railways.shp", "rb")
    mydbf = open(path / "data" / "railways.dbf", "rb")

    sf = shapefile.Reader(shp=myshp, dbf=mydbf)

    rows = sf.shapeRecords()
    print(sf)
