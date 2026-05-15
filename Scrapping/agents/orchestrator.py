"""
ORCHESTRATEUR MULTI-AGENTS A2A
-------------------------------
Coordonne plusieurs agents de scraping pour collecter des données
de plusieurs plateformes en parallèle.
"""

from typing import List, Dict, Any
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from loguru import logger


class A2AOrchestrator:
    """
    Orchestrateur central qui gère la flotte d'agents A2A
    """
    
    def __init__(self):
        self.agents = []          # Liste des agents enregistrés
        self.results = {}         # Résultats par agent
        logger.info("Orchestrateur A2A initialisé")
    
    def register_agent(self, agent):
        """
        ENREGISTRER UN AGENT
        Ajoute un agent à la flotte
        """
        self.agents.append(agent)
        logger.info(f"Agent {agent.agent_id} enregistré")
    
    def run_parallel_scraping(self, categories: List[str], max_workers: int = 3) -> pd.DataFrame:
        """
        SCRAPING PARALLÈLE MULTI-PLATEFORMES
        Lance tous les agents en parallèle avec ThreadPoolExecutor
        """
        all_data = []
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Soumettre toutes les tâches
            future_to_agent = {}
            for agent in self.agents:
                for category in categories:
                    future = executor.submit(agent.scrape_category, category)
                    future_to_agent[future] = (agent, category)
            
            # Récupérer les résultats au fur et à mesure
            for future in as_completed(future_to_agent):
                agent, category = future_to_agent[future]
                try:
                    df = future.result()
                    all_data.append(df)
                    self.results[agent.agent_id] = df
                    logger.success(f"[{agent.agent_id}] {len(df)} produits de {category}")
                except Exception as e:
                    logger.error(f"[{agent.agent_id}] Échec: {e}")
        
        # Fusionner tous les DataFrames
        if all_data:
            final_df = pd.concat(all_data, ignore_index=True)
            logger.info(f"Total collecté: {len(final_df)} produits")
            return final_df
        return pd.DataFrame()
    
    def get_comparative_analysis(self) -> Dict[str, Any]:
        """
        ANALYSE COMPARATIVE ENTRE PLATEFORMES
        Compare les résultats des différents agents
        """
        comparison = {}
        for agent_id, df in self.results.items():
            comparison[agent_id] = {
                'nb_products': len(df),
                'avg_price': df['price'].mean() if 'price' in df.columns else None,
                'avg_rating': df['rating'].mean() if 'rating' in df.columns else None,
                'categories': df['category'].unique().tolist() if 'category' in df.columns else []
            }
        return comparison