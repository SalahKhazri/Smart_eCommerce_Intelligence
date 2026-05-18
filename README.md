# 🧠 Smart eCommerce Intelligence

Projet intelligent de **data mining et MLOps** pour l’analyse, la sélection et la recommandation de produits e-commerce à l’aide du Machine Learning, des LLMs et d’une architecture MCP.

---

## 🚀 Vue d’ensemble du projet

Ce projet a pour objectif de construire un système complet d’intelligence e-commerce capable de :

- 📊 Analyser des données produits
- 🏆 Sélectionner les Top-K produits selon un score
- 🤖 Générer des recommandations intelligentes avec un LLM
- 📈 Visualiser les résultats dans un dashboard interactif
- ⚙️ Automatiser les pipelines ML avec Kubeflow
- 🔐 Implémenter une architecture MCP (Model Context Protocol simplifié)
- 🚀 Ajouter une automatisation CI/CD avec GitHub Actions

---

## 🏗️ Architecture globale
```
Données → Pipeline ML → Dashboard BI → LLM → MCP → CI/CD
```
## Structure du projet

```
Smart_eCommerce_Intelligence/
│
├── .github/
│   ├── workflows/
│   │   └── ml_pipeline.yml
├── dashboard/                      # Interface BI (Streamlit)
│   ├── app.py
│   ├── assets/
│   │   └── style.css
│   ├── components/
│   │   ├── charts.py
│   │   ├── kpi_cards.py
│   │   └── navbar.py
│   └── pages/
│       ├── 1_KPI.py
│       ├── 2_Analytics.py
│       ├── 3_TopK.py
│       └── 4_Recommendations.py
│
├── data/
│   ├── raw/
│   │   └── products.csv
│   └── processed/
│
├── images/
├── LLM/                            # Module IA (LLM + prompts)
│   ├── __init__.py
│   ├── llm_engine.py
│   ├── prompts.py
│   └── recommender.py
│
├── MCP/                            # Architecture MCP (agent system)
│   ├── __init__.py
│   ├── client.py
│   ├── server.py
│   ├── logger.py
│   ├── logs.json
│   ├── permissions.json
│   └── tools.py
│
├── ML/                             # Machine Learning pipeline
│   ├── load_data.py
│   ├── clean_data.py
│   ├── feature_engineering.py
│   ├── normalization.py
│   ├── clustering.py
│   ├── dimensionality.py
│   ├── scoring.py
│   ├── topk_selection.py
│   ├── prediction.py
│   ├── association_rules.py
│   ├── shop_analysis.py
│   ├── visualization.py
│   ├── config.py
│   └── pipeline.py
│
├── ml_pipeline_kubeflow/          # Pipeline Kubeflow (MLOps)
│   ├── compile_pipeline.py
│   ├── ecommerce_pipeline.py
│   ├── ecommerce_pipeline.yaml
│   ├── run_pipeline.py
│   │
│   ├── components/
│   │   ├── load.py
│   │   ├── clean.py
│   │   ├── features.py
│   │   ├── score.py
│   │   ├── topk.py
│   │   └── train.py
│   │
│   └── docker/                        # Images Docker par étape
│       ├── data/
│       │   ├── Dockerfile.data
│       │   └── requirements.txt
│       │
│       ├── ml/
│       │   ├── Dockerfile.ml
│       │   └── requirements.txt
│       │
│       └── serving/
│           ├── Dockerfile.serving
│           └── requirements.txt
│
├── Scrapping/                      # Data collection
│   ├── main.py
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── orchestrator.py
│   │   ├── shopify_agent.py
│   │   └── woocommerce_agent.py
│   ├── data/
│   │   ├── products.csv
│   │   └── products.json
│   └── utils/
│       ├── helpers.py
│       └── __init__.py
│
├── models/                         # Modèles ML sauvegardés
│
├── outputs/                        # Résultats ML
│   ├── association_rules.csv
│   ├── clusters.csv
│   ├── final_products_ml.csv
│   ├── shop_ranking.csv
│   └── topk_products.csv
│
├── reports/                        # Rapports finaux
│   └── topk_products.csv
│
├── .gitignore
├── Dockerfile                      # Container principal
├── main.py                         # Entrée principale (optionnel)
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Cloner le projet

```bash id="clone_fr"
git clone https://github.com/SalahKhazri/Smart_eCommerce_Intelligence.git
cd Smart_eCommerce_Intelligence
```
### 2. Créer un environnement virtuel
```
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate (Linux/Mac)
```
### 3. Installer les dépendances
```
pip install -r requirements.txt
```

## Installation du LLM (Ollama)

- Installer Ollama :

👉 https://ollama.com/download

- Installer llama3

```
ollama pull llama3
```

- Télécharger un modèle :

```
ollama run llama3
```

- Modèle léger recommandé :

```
ollama run phi3
```
## 🚀 Lancer le projet
Lancer le dashboard Streamlit
```
cd dashboard
streamlit run app.py
```

## Fonctionnalités
### 1. Traitement des données
- Nettoyage du dataset produit
- Feature engineering (score de qualité produit)

### 2. Sélection Top-K

-Classement des produits selon un score
-Analyse business des produits les plus performants

### 3. Dashboard BI (Streamlit)
- KPI (indicateurs clés)
- Graphiques interactifs
- Analyse visuelle des tendances
### 4. Recommandation par LLM
- Analyse des produits
- Génération de recommandations intelligentes
- Explications business automatisées
### 5. Architecture MCP (simplifiée)

Le système MCP permet :

- Host : Streamlit (interface principale)
- Client : gestion des requêtes
- Server : orchestration des analyses
- Logger : suivi des actions
- Permissions : contrôle d’accès

### Fonctionnalités MCP
- Journalisation des actions utilisateur
- Sécurisation des accès aux outils
- Traçabilité des requêtes
- Simulation d’agent intelligent

### 6. CI/CD (GitHub Actions)

Automatisation du workflow :

- Vérification du code Python
- Installation des dépendances
- Test du pipeline ML
- Compilation automatique

## Exemple de logs MCP
 ```
 {"time": "2026-05-18", "action": "TOPK_REQUEST", "data": "demande de produits populaires"}
 {"time": "2026-05-18", "action": "LLM_REQUEST", "data": "analyse produit Gymshark"}
 ```

## Docker (optionnel)

Construire l’image :
```
docker build -t smart-ecommerce .
```
Exécuter :
```
docker run -p 8501:8501 smart-ecommerce
```

## Technologies utilisées
- Python 
- Pandas / NumPy
- Streamlit 
- Kubeflow Pipelines 
- Docker 
- GitHub Actions 
- LangChain 
- Ollama (LLM local) 
- MCP (architecture agentique simplifiée)

## Objectifs du projet
- Construire un système complet de Data Science + IA
- Combiner ML + LLM + MLOps
- Simuler une architecture industrielle moderne
- Développer des compétences en IA appliquée


## Auteur

Projet académique : Smart eCommerce Intelligence
Module : Data Mining & MLOps


