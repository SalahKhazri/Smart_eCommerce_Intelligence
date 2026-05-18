# Smart_eCommerce_Intelligence

Projet d'analyse et de recommandation pour e‑commerce — pipeline ML, visualisation et composants LLM.

## Structure du projet

```
Dockerfile
main.py
README.md
requirements.txt
dashboard/
	app.py
	assets/
		style.css
	components/
		charts.py
		kpi_cards.py
		navbar.py
	pages/
		1_KPI.py
		2_Analytics.py
		3_TopK.py
		4_Recommendations.py
data/
	processed/
	raw/
		products.csv
images/
LLM/
	__init__.py
	llm_engine.py
	prompts.py
	recommender.py
MCP/
	__init__.py
	client.py
	logger.py
	logs.json
	permissions.json
	server.py
	tools.py
ML/
	association_rules.py
	clean_data.py
	clustering.py
	config.py
	dimensionality.py
	feature_engineering.py
	load_data.py
	normalization.py
	pipeline.py
	prediction.py
	scoring.py
	shop_analysis.py
	topk_selection.py
	visualization.py
ml_pipeline_kubeflow/
	compile_pipeline.py
	ecommerce_pipeline.py
	ecommerce_pipeline.yaml
	run_pipeline.py
	components/
		clean.py
		features.py
		load.py
		score.py
		topk.py
		train.py
	docker/
		processing/
			Dockerfile
			requirements.txt
		scoring/
			Dockerfile
			requirements.txt
		topk/
			Dockerfile
			requirements.txt
		training/
			Dockerfile
			requirements.txt
models/
outputs/
	association_rules.csv
	clusters.csv
	final_products_ml.csv
	shop_ranking.csv
	topk_products.csv
reports/
	topk_products.csv
Scrapping/
	main.py
	agents/
		__init__.py
		base_agent.py
		orchestrator.py
		shopify_agent.py
		woocommerce_agent.py
	data/
		products.csv
		products.json
	utils/
		__init__.py
		helpers.py

## Fichiers clés

- `main.py` : point d'entrée principal du projet.
- `dashboard/app.py` : application Streamlit pour visualisation et KPI.
- `ML/` : modules pour préparation, modèles et scoring.
- `LLM/` : intégration et prompts pour composants de recommandation basés sur LLM.
- `ml_pipeline_kubeflow/` : pipeline Kubeflow et composants Docker.

## Démarrage rapide

1. Créer un environnement Python et installer les dépendances :

```bash
pip install -r requirements.txt
```

2. Lancer le dashboard (exemple) :

```bash
streamlit run dashboard/app.py
```

---

Si vous voulez, je peux compléter ce README avec des descriptions détaillées pour chaque dossier et des exemples d'utilisation.

