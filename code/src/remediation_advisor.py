class RemediationAdvisor:
    def __init__(self, llm_model):
        self.llm = llm_model
        self.knowledge_base = []

    def suggest_remediation(self, rule_violation, historical_data):
        prompt = f"""
        Given this data quality rule violation:
        {rule_violation}

        And similar historical violations and their resolutions:
        {historical_data}

        Suggest 3 potential remediation actions, ordered by likely effectiveness.
        For each action, estimate implementation complexity (Low/Medium/High).
        """

        suggestions = self.llm.generate(prompt)
        return self._parse_suggestions(suggestions)

    def update_knowledge_base(self, new_resolution):
        self.knowledge_base.append(new_resolution)