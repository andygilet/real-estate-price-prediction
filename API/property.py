from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Property(Base):
    __tablename__ = 'properties'
    
    id = Column("ID", Integer, primary_key=True)
    area = Column("area", Integer)
    property_type = Column("property-type", String(100))
    rooms_number = Column("rooms-number", Integer)
    zip_code = Column("zip-code",Integer)
    land_area = Column("land-area", Integer)
    garden = Column("garden", Boolean)
    garden_area = Column("garden-area", Integer)
    equipped_kitchen = Column("equipped-kitchen", Boolean)
    full_address = Column("full-address", String(100))
    swimming_pool = Column("swimming-pool", Boolean)
    furnished = Column("furnished", Boolean)
    open_fire = Column("open-fire", Boolean)
    terrace = Column("terrace", Boolean)
    terrace_area = Column("terrace-area", Integer)
    facade_number = Column("facade-number", Integer)
    building_state = Column("building-state", String(100))
    
    def __init__(self, area : int, property_type : str, rooms_number : int,
                 zip_code : int, land_area : int, garden : bool, garden_area :int,
                 equipped_kitchen : bool, full_address : str, swimming_pool : bool,
                 furnished : bool, open_fire : bool, terrace : bool, terrace_area : bool,
                 facade_number : int, building_state : str):
        self.area = area
        self.property_type = property_type
        self.rooms_number = rooms_number
        self.zip_code = zip_code
        self.land_area = land_area
        self.garden = garden
        self.garden_area = garden_area
        self.equipped_kitchen = equipped_kitchen
        self.full_address = full_address
        self.swimming_pool = swimming_pool
        self.furnished = furnished
        self.open_fire = open_fire
        self.terrace = terrace
        self.terrace_area = terrace_area
        self.facade_number = facade_number
        self.building_state = building_state
        
    def __repr__(self) -> str:
        return f"({self.ID} {self.area} {self.property_type} {self.rooms_number} {self.zip_code} {self.land_area} {self.garden} {self.garden_area} {self.equipped_kitchen} {self.full_address} {self.swimming_pool} {self.furnished} {self.open_fire} {self.terrace} {self.terrace_area} {self.facade_number} {self.building_state})"

def add_entry(property : Property, session):
    session.add(property)
    session.commit()
    session.close()
        
def get_all_entry(session) -> list:
    properties = session.query(Property).all()
    return properties
    
def get_entry(id : int , session) -> Property:
    property = session.query(Property).filter(Property.id == id)
    return property

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()