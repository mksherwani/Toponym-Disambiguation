# 🌍 Toponym Disambiguation Workflow (Neo4j-Based)

This repository provides a **systematic and reproducible pipeline** for **Toponym Resolution**, leveraging **Neo4j** as the graph database to store and analyze global geographic data. The workflow consists of three key steps:

1️⃣ **Gazetteer to Graphetteer** – Translating the Geonames atlas into a graph database.  
2️⃣ **Toponym Extraction** – Identifying and formatting location names from text.  
3️⃣ **Toponym Resolution** – Resolving locations based on population and spatial relationships.  

Each step is housed in its respective folder, with detailed scripts to ensure reproducibility.

---

## 🗺️ Gazetteer to Graphetteer
**Goal:** Convert the **Geonames atlas** into a **Neo4j graph database** for efficient querying and spatial analysis.

📂 **Scripts included:**
- `import_geonames.py` – Loads Geonames data into Neo4j.
- `link_nodes.py` – Establishes relationships between location nodes.
- `graph_queries.cypher` – Cypher queries to interact with the graph database.

🔹 **Outcome:** A **fully structured geographic knowledge graph**, ready for toponym resolution.

---

## 🔎 Toponym Extraction
**Goal:** Extract and format location names from articles using **Stanford NER**.

📂 **Scripts included:**
- `ner_tagger.py` – Tags location names in text.
- `merge_entities.py` – Merges consecutive tagged entities  
  _(e.g., **United/location Kingdom/location → United Kingdom/location**)_.
- `vertical_format.py` – Converts extracted names into a structured, indexed format.
- `extract_toponyms.py` – Extracts and indexes toponyms per article.

🔹 **Outcome:** A **clean and structured dataset** of extracted location names.

---

## 🌍 Toponym Resolution
**Goal:** Resolve extracted toponyms using three different Neo4j-based approaches.

📂 **Scripts included:**
- `resolve_by_population.py` – Finds the most populated location for each toponym.
- `resolve_by_distance.py` – Calculates pairwise distances and selects the shortest.
- `resolve_by_graph_edges.py` – Resolves toponyms using **graph-based connectivity**, considering **population properties**.

🔹 **Outcome:** A **precise mapping** of location references in articles to real-world locations.

---

## 🚀 How to Use
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
