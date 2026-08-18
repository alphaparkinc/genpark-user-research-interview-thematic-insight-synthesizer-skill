from client import UserResearchInterviewThematicInsightSynthesizerClient

def main():
    client = UserResearchInterviewThematicInsightSynthesizerClient()
    transcripts = ["User A: I spent 2 hours debugging webhook signature format.", "User B: Need better TS types."]
    res = client.synthesize_insights(transcripts)
    print(f"Confidence: {res['confidence_score_pct']}%")
    print("Thematic Clusters:", res["top_thematic_clusters"])
    print("Recommendations:", res["actionable_recommendations"])

if __name__ == "__main__":
    main()
