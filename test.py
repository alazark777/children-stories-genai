initial_state = {
    "messages": [],
    "campaign_context": {
        "content": "Claim your free vacation now! Limited time offer, click to book!",
        "ml_prediction": "positive",
        "policy_flag": "triggered"
    },
    "user_id": "user_003",
    "similar_campaigns": {},
    "user_info": {},
    "final_decision": {}
}
result = app.invoke(initial_state)
print(result["user_info"])
print(result["final_decision"])
