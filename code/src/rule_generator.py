from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np


class RuleGenerator:
    def __init__(self, llm_model):
        self.llm = llm_model
        self.rules = []

    def generate_profiling_rules(self, data_sample, requirements):
        # Step 1: Use LLM to suggest initial rules based on requirements
        llm_rules = self._get_llm_suggested_rules(data_sample, requirements)

        # Step 2: Apply unsupervised learning to discover data patterns
        ml_rules = self._discover_data_patterns(data_sample)

        # Combine and deduplicate rules
        combined_rules = self._merge_rules(llm_rules, ml_rules)

        return combined_rules

    def _get_llm_suggested_rules(self, data_sample, requirements):
        prompt = f"""
        Based on these regulatory requirements:
        {requirements}

        And this sample data structure:
        {data_sample.head(3).to_dict()}

        Generate data profiling rules that would validate compliance.
        Include rules for:
        - Completeness
        - Validity
        - Consistency
        - Timeliness

        Format as JSON with rule_type, field, condition, and error_message.
        """

        response = self.llm.generate(prompt)
        return self._parse_llm_response(response)

    def _discover_data_patterns(self, data):
        # Numeric field clustering for outlier detection
        numeric_cols = data.select_dtypes(include=np.number).columns
        rules = []

        for col in numeric_cols:
            # Use DBSCAN to find outliers
            values = data[col].values.reshape(-1, 1)
            clustering = DBSCAN(eps=3, min_samples=2).fit(values)

            # Create rules based on clusters
            if len(set(clustering.labels_)) > 1:
                min_val = data[col].min()
                max_val = data[col].max()
                rules.append({
                    "rule_type": "validity",
                    "field": col,
                    "condition": f"value >= {min_val} and value <= {max_val}",
                    "error_message": f"{col} value outside expected range"
                })

        return rules