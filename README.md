# Neo4j Connection Script

## Overview
This script connects to a Neo4j database and inserts sample data representing a social graph of people and their friendships.

## Prerequisites
- Python 3.7+
- Neo4j database (AuraDB or self-hosted)
- Installed dependencies: `neo4j`

## Installation
1. **Clone the repository** (if applicable):
   ```sh
   git clone https://github.com/anubhavanand1516/neo4j_sample.git
   cd neo4j_sample
   ```
2. **Install dependencies**:
   ```sh
   pip install neo4j
   ```

## Configuration
Update the following variables in `neo4j_connect.py` with your Neo4j credentials:
```python
URI = "neo4j+s://your-database-uri"
USERNAME = "your-username"
PASSWORD = "your-password"
```
For better security, use environment variables instead of hardcoding credentials.

## Usage
Run the script to insert the sample graph data:
```sh
python neo4j_main.py
```

## Expected Output
If successful, the script will print:
```
✅ Graph Data Inserted Successfully!
```
## All Node
![visualisation](https://github.com/user-attachments/assets/97d0575a-c054-424b-9fef-0420a1dd369e)

## Relationships
![visualisation (1)](https://github.com/user-attachments/assets/aa6bbc0f-8995-45b6-b8f4-53775ed800df)

## Functionality
- **Establishes connection** to Neo4j using the `GraphDatabase` driver.
- **Runs Cypher queries** using the `run_query` function.
- **Creates a sample graph** with `Person` nodes and `FRIENDS_WITH` relationships.

## Notes
- Ensure that your Neo4j database is running and accessible.
- If using Neo4j AuraDB, ensure the correct connection URI format.
- Modify the script to handle different graph structures as needed.



