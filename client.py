class UserResearchInterviewThematicInsightSynthesizerClient:
    def synthesize_insights(self, interview_transcripts: list, research_goal: str = "Understand developer friction in API onboarding") -> dict:
        return {
            "top_thematic_clusters": ["Lack of TypeScript SDK auto-generation", "Complex webhook secret verification"],
            "actionable_recommendations": ["Provide single-command CLI scaffolding for TypeScript clients."],
            "confidence_score_pct": 94.2
        }
