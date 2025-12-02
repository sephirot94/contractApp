from app.database import SessionLocal
from app.models import Contractor, ContractorType, PriceRange

def seed_database():
    """Seed the database with sample contractor data."""
    db = SessionLocal()

    # Check if data already exists
    if db.query(Contractor).first():
        print("Database already contains data. Skipping seed.")
        db.close()
        return

    # Sample contractors in Sydney area
    contractors = [
        # Electricians
        Contractor(
            name="Bright Spark Electrical",
            specialty=ContractorType.ELECTRICIAN,
            location="Sydney CBD",
            latitude=-33.8688,
            longitude=151.2093,
            price_range=PriceRange.MEDIUM,
            phone="+61 2 1234 5678",
            email="contact@brightspark.com.au",
            description="Licensed electricians with 20+ years experience"
        ),
        Contractor(
            name="Power Solutions",
            specialty=ContractorType.ELECTRICIAN,
            location="Parramatta",
            latitude=-33.8151,
            longitude=150.9989,
            price_range=PriceRange.HIGH,
            phone="+61 2 2234 5678",
            email="info@powersolutions.com.au",
            description="Commercial and residential electrical services"
        ),
        Contractor(
            name="QuickFix Electrics",
            specialty=ContractorType.ELECTRICIAN,
            location="Bondi",
            latitude=-33.8908,
            longitude=151.2743,
            price_range=PriceRange.LOW,
            phone="+61 2 3234 5678",
            email="hello@quickfix.com.au",
            description="Fast and affordable electrical repairs"
        ),

        # Plumbers
        Contractor(
            name="Pro Plumbing Services",
            specialty=ContractorType.PLUMBER,
            location="Sydney CBD",
            latitude=-33.8650,
            longitude=151.2094,
            price_range=PriceRange.MEDIUM,
            phone="+61 2 4234 5678",
            email="service@proplumbing.com.au",
            description="24/7 emergency plumbing services"
        ),
        Contractor(
            name="Waterworks Plumbing",
            specialty=ContractorType.PLUMBER,
            location="Chatswood",
            latitude=-33.7969,
            longitude=151.1831,
            price_range=PriceRange.HIGH,
            phone="+61 2 5234 5678",
            email="contact@waterworks.com.au",
            description="Premium plumbing and drainage solutions"
        ),
        Contractor(
            name="Budget Plumbers",
            specialty=ContractorType.PLUMBER,
            location="Penrith",
            latitude=-33.7507,
            longitude=150.6937,
            price_range=PriceRange.LOW,
            phone="+61 2 6234 5678",
            email="info@budgetplumbers.com.au",
            description="Affordable plumbing for western suburbs"
        ),

        # Gas Fitters
        Contractor(
            name="SafeGas Solutions",
            specialty=ContractorType.GAS,
            location="Sydney CBD",
            latitude=-33.8705,
            longitude=151.2080,
            price_range=PriceRange.PREMIUM,
            phone="+61 2 7234 5678",
            email="safety@safegas.com.au",
            description="Certified gas fitting and safety inspections"
        ),
        Contractor(
            name="Metro Gas Services",
            specialty=ContractorType.GAS,
            location="Hurstville",
            latitude=-33.9676,
            longitude=151.1022,
            price_range=PriceRange.MEDIUM,
            phone="+61 2 8234 5678",
            email="contact@metrogas.com.au",
            description="Gas appliance installation and repairs"
        ),

        # Builders
        Contractor(
            name="Premier Builders",
            specialty=ContractorType.BUILDER,
            location="Sydney CBD",
            latitude=-33.8700,
            longitude=151.2100,
            price_range=PriceRange.PREMIUM,
            phone="+61 2 9234 5678",
            email="projects@premierbuilders.com.au",
            description="High-end residential and commercial construction"
        ),
        Contractor(
            name="Solid Construction",
            specialty=ContractorType.BUILDER,
            location="Liverpool",
            latitude=-33.9210,
            longitude=150.9234,
            price_range=PriceRange.MEDIUM,
            phone="+61 2 0234 5678",
            email="info@solidconstruction.com.au",
            description="Quality home renovations and extensions"
        ),
        Contractor(
            name="EcoBuilders",
            specialty=ContractorType.BUILDER,
            location="Manly",
            latitude=-33.7969,
            longitude=151.2840,
            price_range=PriceRange.HIGH,
            phone="+61 2 1111 5678",
            email="hello@ecobuilders.com.au",
            description="Sustainable and eco-friendly building solutions"
        ),
        Contractor(
            name="Quick Renos",
            specialty=ContractorType.BUILDER,
            location="Bankstown",
            latitude=-33.9167,
            longitude=151.0345,
            price_range=PriceRange.LOW,
            phone="+61 2 2222 5678",
            email="contact@quickrenos.com.au",
            description="Fast and affordable renovation services"
        ),
    ]

    db.add_all(contractors)
    db.commit()
    print(f"Successfully seeded {len(contractors)} contractors")
    db.close()

if __name__ == "__main__":
    seed_database()
