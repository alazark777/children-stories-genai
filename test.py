from langchain_core.tools import tool
from typing import Dict, Any
from typing_extensions import TypedDict

# Simulated user database
USER_DATABASE = {
    "user_001": {
        "user_id": "user_001",
        "is_new_user": True,
        "campaign_count": 1,
        "previous_spam_count": 0
    },
    "user_002": {
        "user_id": "user_002",
        "is_new_user": False,
        "campaign_count": 10,
        "previous_spam_count": 2
    },
    "user_003": {
        "user_id": "user_003",
        "is_new_user": False,
        "campaign_count": 5,
        "previous_spam_count": 1
    },
    "user_004": {
        "user_id": "user_004",
        "is_new_user": True,
        "campaign_count": 3,
        "previous_spam_count": 0
    },
    "user_005": {
        "user_id": "user_005",
        "is_new_user": False,
        "campaign_count": 15,
        "previous_spam_count": 5
    }
}

# LangChain tool to fetch user info
@tool
def fetch_user_info_tool(user_id: str) -> Dict[str, Any]:
    """
    Fetches user information from a simulated database by user ID.
    
    Args:
        user_id: The ID of the user to retrieve information for.
    
    Returns:
        A dictionary containing user information or an empty dict if not found.
    """
    return USER_DATABASE.get(user_id, {})

# Updated fetch_user_info node
def fetch_user_info(state: AgentState) -> Dict[str, Any]:
    print("---FETCH USER INFO---")
    user_id = state["user_id"]
    user_info = fetch_user_info_tool.invoke({"user_id": user_id})
    return {"user_info": user_info}
