import csv
import os
from sqlalchemy.orm import sessionmaker
from database import engine, init_db
from models import Bank, Branch

def ingest_csv(filename):
    # Initialize the database first
    init_db()

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Check if the file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file {filename} does not exist.")

        with open(filename, 'r') as f:
            csv_reader = csv.DictReader(f)
            banks = {}
            for row in csv_reader:
                bank_id = int(row['bank_id'])
                if bank_id not in banks:
                    bank = Bank(id=bank_id, name=row['bank_name'])
                    session.add(bank)
                    banks[bank_id] = bank
                
                branch = Branch(
                    ifsc=row['ifsc'],
                    bank_id=bank_id,
                    branch=row['branch'],
                    address=row['address'],
                    city=row['city'],
                    district=row['district'],
                    state=row['state']
                )
                session.add(branch)

            session.commit()
            print(f"Successfully ingested data from {filename}")
    except Exception as e:
        print(f"An error occurred while ingesting data: {str(e)}")
        session.rollback()
    finally:
        session.close()

if __name__ == '__main__':
    ingest_csv('bank_branches.csv')

