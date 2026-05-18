from LLM.prompts import PRODUCT_ANALYSIS_PROMPT
from LLM.llm_engine import generate_response

def analyze_product(product):

    prompt = PRODUCT_ANALYSIS_PROMPT.format(
        title=product["title"],
        category=product["category"],
        price=product["price"],
        score=product["score"]
    )

    return generate_response(prompt)