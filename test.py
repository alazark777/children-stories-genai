def retrieve(state: AgentState) -> Dict[str, Any]:
    print("---RETRIEVE SIMILAR CAMPAIGNS---")
    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls:
        tool_call = last_message.tool_calls[0]
        if tool_call["name"] == "retrieve_similar_campaigns":
            query = tool_call["args"].get("query", state["campaign_context"]["content"])
            results = retrieve_similar_campaigns.invoke(query)
            campaigns = []
            for doc in results.split("\n\n"):
                campaign = {}
                lines = doc.split("\n")
                for line in lines:
                    if ": " not in line:
                        continue
                    key, value = line.split(": ", 1)
                    if key == "Campaign ID":
                        campaign["campaign_id"] = value
                    elif key == "Content":
                        campaign["content"] = value
                    elif key == "Human Review Label":
                        campaign["human_review_label"] = value
                    elif key == "ML Prediction":
                        campaign["ml_prediction"] = value
                    elif key == "Policy Flag":
                        campaign["policy_flag"] = value
                if campaign:
                    campaigns.append(campaign)
            return {"similar_campaigns": {"campaigns": campaigns}}
    return {"similar_campaigns": {}}
