from app.constants import Specialty
from app.database import SessionLocal
from app.models import City, Contractor, PriceRange


def seed_database():
    """Seed the database with sample contractor and city data."""
    db = SessionLocal()

    # Check if data already exists
    if db.query(City).first():
        print("Database already contains data. Skipping seed.")
        db.close()
        return

    # Create Latin American cities
    cities = [
        City(name="Buenos Aires", country="Argentina"),
        City(name="São Paulo", country="Brazil"),
        City(name="Mexico City", country="Mexico"),
        City(name="Lima", country="Peru"),
        City(name="Bogotá", country="Colombia"),
        City(name="Santiago", country="Chile"),
    ]

    db.add_all(cities)
    db.commit()
    print(f"Successfully seeded {len(cities)} cities")

    # Refresh to get IDs
    for city in cities:
        db.refresh(city)

    # Sample contractors for each city
    # Buenos Aires contractors (city_id=1)
    buenos_aires = next(c for c in cities if c.name == "Buenos Aires")
    contractors = [
        # Buenos Aires - Palermo
        Contractor(
            name="ElectroBA",
            specialty=Specialty.ELECTRICITY,
            location="Palermo",
            latitude=-34.5889,
            longitude=-58.4194,
            price_range=PriceRange.MEDIUM,
            phone="+54 11 1234 5678",
            email="contacto@electroba.com.ar",
            description="Electricistas profesionales con 15 años de experiencia",
            city_id=buenos_aires.id,
        ),
        Contractor(
            name="PlomeroExpress",
            specialty=Specialty.PLUMBING,
            location="Recoleta",
            latitude=-34.5875,
            longitude=-58.3974,
            price_range=PriceRange.LOW,
            phone="+54 11 2234 5678",
            email="info@plomeroexpress.com.ar",
            description="Servicio de plomería 24/7",
            city_id=buenos_aires.id,
        ),
        Contractor(
            name="Gas Seguro BA",
            specialty=Specialty.GAS,
            location="San Telmo",
            latitude=-34.6211,
            longitude=-58.3724,
            price_range=PriceRange.HIGH,
            phone="+54 11 3234 5678",
            email="contacto@gasseguro.com.ar",
            description="Instalaciones de gas certificadas",
            city_id=buenos_aires.id,
        ),
        Contractor(
            name="Constructora del Sur",
            specialty=Specialty.CONSTRUCTION,
            location="Belgrano",
            latitude=-34.5633,
            longitude=-58.4575,
            price_range=PriceRange.PREMIUM,
            phone="+54 11 4234 5678",
            email="proyectos@constructoradelsur.com.ar",
            description="Construcción y remodelaciones de alta gama",
            city_id=buenos_aires.id,
        ),
    ]

    # São Paulo contractors (city_id=2)
    sao_paulo = next(c for c in cities if c.name == "São Paulo")
    contractors.extend(
        [
            Contractor(
                name="Elétrica Paulista",
                specialty=Specialty.ELECTRICITY,
                location="Paulista Avenue",
                latitude=-23.5629,
                longitude=-46.6544,
                price_range=PriceRange.MEDIUM,
                phone="+55 11 91234 5678",
                email="contato@eletricapaulista.com.br",
                description="Serviços elétricos residenciais e comerciais",
                city_id=sao_paulo.id,
            ),
            Contractor(
                name="Encanador Rápido",
                specialty=Specialty.PLUMBING,
                location="Vila Madalena",
                latitude=-23.5505,
                longitude=-46.6888,
                price_range=PriceRange.LOW,
                phone="+55 11 92234 5678",
                email="contato@encanadorrapido.com.br",
                description="Desentupimentos e reparos hidráulicos",
                city_id=sao_paulo.id,
            ),
            Contractor(
                name="Carpintaria Arte em Madeira",
                specialty=Specialty.CARPENTRY,
                location="Pinheiros",
                latitude=-23.5668,
                longitude=-46.7014,
                price_range=PriceRange.HIGH,
                phone="+55 11 93234 5678",
                email="contato@artemadeira.com.br",
                description="Móveis planejados e carpintaria fina",
                city_id=sao_paulo.id,
            ),
            Contractor(
                name="Jardins Tropicais",
                specialty=Specialty.GARDENING,
                location="Jardins",
                latitude=-23.5648,
                longitude=-46.6731,
                price_range=PriceRange.MEDIUM,
                phone="+55 11 94234 5678",
                email="contato@jardinstropicais.com.br",
                description="Paisagismo e manutenção de jardins",
                city_id=sao_paulo.id,
            ),
        ]
    )

    # Mexico City contractors (city_id=3)
    mexico_city = next(c for c in cities if c.name == "Mexico City")
    contractors.extend(
        [
            Contractor(
                name="Electricistas CDMX",
                specialty=Specialty.ELECTRICITY,
                location="Polanco",
                latitude=19.4326,
                longitude=-99.1919,
                price_range=PriceRange.MEDIUM,
                phone="+52 55 1234 5678",
                email="contacto@electricistascdmx.mx",
                description="Instalaciones eléctricas certificadas",
                city_id=mexico_city.id,
            ),
            Contractor(
                name="Plomería Azteca",
                specialty=Specialty.PLUMBING,
                location="Roma Norte",
                latitude=19.4188,
                longitude=-99.1641,
                price_range=PriceRange.LOW,
                phone="+52 55 2234 5678",
                email="info@plomeriazteca.mx",
                description="Reparaciones y mantenimiento de plomería",
                city_id=mexico_city.id,
            ),
            Contractor(
                name="Limpieza Total",
                specialty=Specialty.CLEANING,
                location="Condesa",
                latitude=19.4098,
                longitude=-99.1719,
                price_range=PriceRange.LOW,
                phone="+52 55 3234 5678",
                email="contacto@limpiezatotal.mx",
                description="Servicios de limpieza profesional",
                city_id=mexico_city.id,
            ),
            Contractor(
                name="Logística Express MX",
                specialty=Specialty.LOGISTIC,
                location="Santa Fe",
                latitude=19.3597,
                longitude=-99.2619,
                price_range=PriceRange.MEDIUM,
                phone="+52 55 4234 5678",
                email="contacto@logisticaexpress.mx",
                description="Mudanzas y transporte de carga",
                city_id=mexico_city.id,
            ),
        ]
    )

    # Lima contractors (city_id=4)
    lima = next(c for c in cities if c.name == "Lima")
    contractors.extend(
        [
            Contractor(
                name="Electro Lima",
                specialty=Specialty.ELECTRICITY,
                location="Miraflores",
                latitude=-12.1192,
                longitude=-77.0350,
                price_range=PriceRange.MEDIUM,
                phone="+51 1 234 5678",
                email="contacto@electrolima.pe",
                description="Electricistas certificados en Lima",
                city_id=lima.id,
            ),
            Contractor(
                name="Gasfiteros del Perú",
                specialty=Specialty.PLUMBING,
                location="San Isidro",
                latitude=-12.0922,
                longitude=-77.0364,
                price_range=PriceRange.MEDIUM,
                phone="+51 1 334 5678",
                email="info@gasfiterosperu.pe",
                description="Gasfitería y mantenimiento",
                city_id=lima.id,
            ),
            Contractor(
                name="Construcciones Inca",
                specialty=Specialty.CONSTRUCTION,
                location="San Borja",
                latitude=-12.0978,
                longitude=-77.0011,
                price_range=PriceRange.HIGH,
                phone="+51 1 434 5678",
                email="proyectos@construccionesinca.pe",
                description="Construcción de casas y edificios",
                city_id=lima.id,
            ),
        ]
    )

    # Bogotá contractors (city_id=5)
    bogota = next(c for c in cities if c.name == "Bogotá")
    contractors.extend(
        [
            Contractor(
                name="Electricidad Bogotá",
                specialty=Specialty.ELECTRICITY,
                location="Chapinero",
                latitude=4.6533,
                longitude=-74.0636,
                price_range=PriceRange.MEDIUM,
                phone="+57 1 234 5678",
                email="contacto@electricidadbogota.co",
                description="Servicios eléctricos profesionales",
                city_id=bogota.id,
            ),
            Contractor(
                name="Plomería Colombia",
                specialty=Specialty.PLUMBING,
                location="Usaquén",
                latitude=4.7110,
                longitude=-74.0301,
                price_range=PriceRange.LOW,
                phone="+57 1 334 5678",
                email="info@plomeriacolombia.co",
                description="Plomería residencial y comercial",
                city_id=bogota.id,
            ),
            Contractor(
                name="Carpinteros Andinos",
                specialty=Specialty.CARPENTRY,
                location="Zona Rosa",
                latitude=4.6679,
                longitude=-74.0544,
                price_range=PriceRange.HIGH,
                phone="+57 1 434 5678",
                email="contacto@carpinterosandinos.co",
                description="Carpintería fina y muebles a medida",
                city_id=bogota.id,
            ),
        ]
    )

    # Santiago contractors (city_id=6)
    santiago = next(c for c in cities if c.name == "Santiago")
    contractors.extend(
        [
            Contractor(
                name="Eléctrica Santiago",
                specialty=Specialty.ELECTRICITY,
                location="Providencia",
                latitude=-33.4305,
                longitude=-70.6100,
                price_range=PriceRange.MEDIUM,
                phone="+56 2 2234 5678",
                email="contacto@electricasantiago.cl",
                description="Instalaciones eléctricas certificadas SEC",
                city_id=santiago.id,
            ),
            Contractor(
                name="Gasfitería Las Condes",
                specialty=Specialty.PLUMBING,
                location="Las Condes",
                latitude=-33.4172,
                longitude=-70.5848,
                price_range=PriceRange.HIGH,
                phone="+56 2 3234 5678",
                email="info@gasfiterialascondes.cl",
                description="Gasfitería premium en Santiago",
                city_id=santiago.id,
            ),
            Contractor(
                name="Jardinería del Valle",
                specialty=Specialty.GARDENING,
                location="Vitacura",
                latitude=-33.3875,
                longitude=-70.5758,
                price_range=PriceRange.HIGH,
                phone="+56 2 4234 5678",
                email="contacto@jardineriadelvalle.cl",
                description="Diseño y mantención de jardines",
                city_id=santiago.id,
            ),
        ]
    )

    db.add_all(contractors)
    db.commit()
    print(f"Successfully seeded {len(contractors)} contractors")
    db.close()


if __name__ == "__main__":
    seed_database()
