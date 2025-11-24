# 🗄️ Ontology Database Stack

This Docker Compose setup provides a complete database stack for the ontology project with Neo4j, Qdrant, MinIO, and Redis.

## 📋 Prerequisites

- 🐋 Docker
- 🐳 Docker Compose
- 📝 `.env` file with required configuration (see Configuration section)

## ⚙️ Configuration

Create a `.env` file in the same directory with the following variables (customize the ports and credentials as needed):

```env
# Neo4j Configuration
NEO4J_HTTP_PORT=<NEO4J_HTTP_PORT>          # Example: 57474 (default is 7474 but avoid it)
NEO4J_BOLT_PORT=<NEO4J_BOLT_PORT>          # Example: 57687 (default is 7687 but avoid it)
NEO4J_AUTH=<neo4j/PASSWORD>                # Example: neo4j/neo4jpassword  (id must be 'neo4j' and password must be longer than 8 characters)

# Qdrant Configuration
QDRANT_PORT=<QDRANT_PORT>                  # Example: 56333 (default is 6333)

# MinIO Configuration
MINIO_PORT=<MINIO_PORT>                       # Example: 59000 (default is 9000 but avoid it)
MINIO_CONSOLE_PORT=<MINIO_CONSOLE_PORT>       # Example: 59090 (default is 9090 but avoid it)
MINIO_ROOT_USER=<MINIO_ROOT_USER>             # Example: minioadmin
MINIO_ROOT_PASSWORD=<MINIO_ROOT_PASSWORD>     # Example: minioadmin

# Redis Configuration
REDIS_PORT=<REDIS_PORT>                       # Example: 56379 (default is 6379 but avoid it)

# Redis Insight Configuration
REDIS_INSIGHT_PORT=<REDIS_INSIGHT_PORT>       # Example: 55540 (default is 5540 but avoid it)
```

**⚠️ Note**: The port numbers and credentials shown are examples. Use your own values to avoid conflicts with other services.

## 🚀 Quick Start

1. 📂 Navigate to the directory containing `compose.yaml`:
   ```bash
   cd ontology_dbs_docker
   ```

2. ▶️ Start all services:
   ```bash
   docker compose up -d
   ```

3. ⏹️ Stop all services:
   ```bash
   docker compose down
   ```

## 🌐 Access Web Interfaces

Once the services are running, access the following GUIs (URLs will vary based on your `.env` configuration):

| Service | URL Pattern | Default Credentials |
|---------|-----|---------------------|
| **🕸️ Neo4j Browser** | http://localhost:{NEO4J_HTTP_PORT}/browser/ | Username: `neo4j`<br>Password: (set in `.env`) |
| **🔍 Qdrant Dashboard** | http://localhost:{QDRANT_PORT}/dashboard | No authentication required |
| **🪣 MinIO Console** | http://localhost:{MINIO_CONSOLE_PORT}/browser | Username: (set in `.env`)<br>Password: (set in `.env`) |
| **📊 Redis Insight** | http://localhost:{REDIS_INSIGHT_PORT}/ | No authentication required |

**💡 Example** (using the sample ports from the Configuration section):
- 🕸️ Neo4j: http://localhost:57474/browser/
- 🔍 Qdrant: http://localhost:56333/dashboard
- 🪣 MinIO: http://localhost:59090/browser
- 📊 Redis Insight: http://localhost:55540/

## 🛠️ Service Details

### 🕸️ Neo4j (Graph Database)
- **Features**: APOC plugin enabled
- **Use Case**: Knowledge graph and relationship management

### 🔍 Qdrant (Vector Database)
- **Use Case**: Vector similarity search and embeddings storage

### 🪣 MinIO (Object Storage)
- **Use Case**: File and object storage (S3-compatible)

### ⚡ Redis (Cache/Message Broker)
- **Features**: Data persistence enabled (saves every 60s if 1+ keys changed)
- **Use Case**: Caching and message queuing

### 📊 Redis Insight (Redis GUI)
- **Use Case**: Redis database visualization and management

## 💾 Data Persistence

All data is stored in Docker-managed volumes and will persist across container restarts:
- 🕸️ `neo4j_conf`, `neo4j_data`, `neo4j_plugins`, `neo4j_logs`
- 🔍 `qdrant_storage`
- 🪣 `minio_config`, `minio_data1-4`
- ⚡ `redis_data`
- 📊 `redis_insight_data`

## 🎯 Useful Commands

### 📜 View logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f neo4j_ontology
```

### 🔄 Restart a service
```bash
docker compose restart neo4j_ontology
```

### 🗑️ Remove all containers and volumes (⚠️ deletes all data)
```bash
docker compose down -v
```

### 📋 List volumes
```bash
docker volume ls | grep ontology
```

## 🌐 Network

All services are connected via the `a2g_ontology_net` network, allowing inter-service communication.

## 🔧 Troubleshooting

### ❌ Service won't start
Check logs: `docker compose logs <service_name>`

### 🚫 Port already in use
Modify the ports in `.env` file and restart services

### 🔒 Permission errors
The compose file uses Docker-managed volumes to avoid permission issues. No manual setup required.

## 📝 Notes

- ♻️ All services are configured with `restart: unless-stopped` for automatic recovery
- 🛡️ MinIO uses erasure coding with 4 data volumes for redundancy
- 🔌 Neo4j includes APOC plugin for advanced graph operations
