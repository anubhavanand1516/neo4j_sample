from neo4j import GraphDatabase

# Neo4j Credentials
URI = "neo4j+s://b6c73605.databases.neo4j.io"  # Your Neo4j AuraDB URI
USERNAME = "neo4j"
PASSWORD = "LG4SKmgWPK4ZcfubPg9kk88OQINJufxolLLvojh7Qow"  # Replace with your actual password

# Connect to Neo4j
driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# Function to run Cypher queries
def run_query(query, parameters=None):
    if parameters is None:
        parameters = {}
    with driver.session() as session:
        session.run(query, parameters)

# Insert Sample Data (Creating People and Relationships)
def create_sample_graph():
    query = """
    CREATE (a:Person {name: 'Alice'})
    CREATE (b:Person {name: 'Bob'})
    CREATE (c:Person {name: 'Charlie'})
    CREATE (a)-[:FRIENDS_WITH]->(b)
    CREATE (b)-[:FRIENDS_WITH]->(c)
    CREATE (c)-[:FRIENDS_WITH]->(a)
    """
    run_query(query)
    print("✅ Graph Data Inserted Successfully!")

# Run the script
if __name__ == "__main__":
    create_sample_graph()
    driver.close()
