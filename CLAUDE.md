# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Docker Compose-based database infrastructure stack ("ontology") for a knowledge graph / ontology project. It contains no application code — only container orchestration configuration for four services: Neo4j, Qdrant, MinIO, and Redis Stack.

## Common Commands

All commands run from `ontology_dbs_docker/`:

```bash
# Start all services
docker compose up -d

# Stop all services
docker compose down

# Stop and delete all data
docker compose down -v

# View logs (all or specific service)
docker compose logs -f
docker compose logs -f neo4j_ontology

# Restart a specific service
docker compose restart neo4j_ontology
```

## Architecture

Four containerized services on a shared Docker network (`ontology_net`):

| Service | Container Name | Purpose | Internal Ports |
|---------|---------------|---------|----------------|
| **Neo4j 5.26.18** | `neo4j_ontology` | Graph database for knowledge graphs | 7474 (HTTP), 7687 (Bolt) |
| **Qdrant** | `qdrant_ontology` | Vector database for embeddings/similarity search | 6333 (REST) |
| **MinIO** | `minio_ontology` | S3-compatible object storage (4-volume erasure coding) | 9000 (API), 9090 (Console) |
| **Redis Stack** | `redis_stack_ontology` | Cache/message broker + RedisInsight GUI | 6379 (Redis), 8001 (RedisInsight) |

Neo4j has APOC and Graph Data Science plugins enabled with unrestricted procedures (`apoc.*`, `gds.*`). The GDS plugin JAR lives in `ontology_dbs_docker/neo4j_plugins/`. There is a commented-out alternative Neo4j config in compose.yaml for manual GDS plugin mounting via bind mount instead of Docker-managed volume.

## Configuration

All ports and credentials are externalized via `ontology_dbs_docker/.env`. Environment variable names are prefixed with `ONTOLOGY_` (e.g., `ONTOLOGY_NEO4J_HTTP_PORT`). See `.env_example` for the template. The README.md uses slightly different variable names than what compose.yaml actually uses — always reference compose.yaml and `.env_example` as the source of truth.

## Data Persistence

All services use Docker-managed named volumes (not bind mounts). Volumes survive `docker compose down` but are destroyed by `docker compose down -v`.

## No Git

All Git operations (pull, push, etc..) are to be done by users. DO NOT try to do any Git operations.
