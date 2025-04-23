import streamlit as st
from content_moderation_workflow import app, AgentState
from typing import Dict, Any

# Streamlit app
st.title("Content Moderation Agentic RAG Demo")
st.write("Enter campaign content to classify it as 'spam', 'not_spam', or 'escalate for human review'.")

# Text input for campaign content
campaign_content = st.text_area("Campaign Content", 
    placeholder="e.g., Limited time offer: Save 50% on your first order at TrendyFashion! Shop now with code SAVE50.")

# Button to trigger moderation
if st.button("Moderate Content"):
    if not campaign_content.strip():
        st.error("Please enter campaign content.")
    else:
        # Construct initial_state
        initial_state: AgentState = {
            "messages": [],
            "campaign_context": {
                "content": campaign_content.strip(),
                "ml_prediction": "positive",
                "policy_flag": "triggered"
            },
            "user_id": "user_005",  # User with high spam history
            "similar_campaigns": {},
            "user_info": {},
            "final_decision": {}
        }

        # Run the LangGraph workflow
        try:
            with st.spinner("Processing..."):
                result = app.invoke(initial_state)
            
            # Display results
            st.subheader("Moderation Result")
            final_decision = result["final_decision"]
            st.write(f"**Decision**: {final_decision['decision']}")
            st.write(f"**Explanation**: {final_decision['explanation']}")
            
            # Display additional context
            with st.expander("View Details"):
                st.write("**Similar Campaigns**:")
                campaigns = result["similar_campaigns"].get("campaigns", [])
                if campaigns:
                    for campaign in campaigns:
                        st.write(f"- Campaign ID: {campaign['campaign_id']}")
                        st.write(f"  Content: {campaign['content']}")
                        st.write(f"  Human Review Label: {campaign['human_review_label']}")
                        st.write(f"  ML Prediction: {campaign['ml_prediction']}")
                        st.write(f"  Policy Flag: {campaign['policy_flag']}")
                else:
                    st.write("No similar campaigns found.")
                
                st.write("**User Info**:")
                user_info = result["user_info"]
                if user_info:
                    st.write(f"- User ID: {user_info.get('user_id', 'N/A')}")
                    st.write(f"- Is New User: {user_info.get('is_new_user', 'N/A')}")
                    st.write(f"- Campaign Count: {user_info.get('campaign_count', 'N/A')}")
                    st.write(f"- Previous Spam Count: {user_info.get('previous_spam_count', 'N/A')}")
                else:
                    st.write("No user info available.")
        except Exception as e:
            st.error(f"Error processing content: {str(e)}")

# Instructions
st.markdown("""
### How It Works
1. Enter campaign content in the text box above.
2. Click "Moderate Content" to analyze the campaign.
3. The system uses an Agentic RAG workflow to:
   - Retrieve similar campaigns from a database.
   - Assess if the context is sufficient to decide.
   - Fetch user information if needed (e.g., for user_005 with a history of spam).
   - Make a final decision: 'spam', 'not_spam', or 'escalate for human review'.
4. View the decision, explanation, and supporting details (similar campaigns and user info).
""")
