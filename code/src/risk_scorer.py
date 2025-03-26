from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


class RiskScorer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = IsolationForest(contamination=0.1)

    def calculate_risk_scores(self, data_violations):
        # Convert violations to features
        features = self._create_features(data_violations)

        # Calculate risk scores
        scaled_features = self.scaler.fit_transform(features)
        scores = self.model.fit_predict(scaled_features)

        # Normalize to 0-100 scale
        risk_scores = (1 - (scores + 1) / 2) * 100
        return risk_scores

    def _create_features(self, violations):
        # Create feature vector based on:
        # - Frequency of violations
        # - Severity of violations
        # - Recency of violations
        # - Regulatory importance

        features = []
        for v in violations:
            feature_vec = [
                v['frequency'],
                v['severity'],
                v['recency'],
                v['regulatory_importance']
            ]
            features.append(feature_vec)

        return np.array(features)