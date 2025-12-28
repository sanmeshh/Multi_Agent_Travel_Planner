from typing import Dict, List, Optional
from pydantic import BaseModel
from schemas.preferences import UserPreference
from schemas.group_preferences import ResolvedGroupPreference

class TripState(BaseModel):
    users: List[str]
    preferences: Dict[str, UserPreference] = {}
    current_user: Optional[str] = None
    current_message: Optional[str] = None
    resolved: Optional[ResolvedGroupPreference] = None
