from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

class Specialization(str, Enum):
    Digital_marketing = "Digital marketing"
    Machine_learning = "Machine learning"
    UX_design = "UX Design"

class TimeZone(str, Enum):
    HST_HDT = "Hawaii-Aleutian Time (HST or HDT)"
    AKST_AKDT = "Alaska Time (AKST or AKDT)"
    PST_PDT = "Pacific Time (PST or PDT)"
    MST_MDT = "Mountain Time (MST or MDT)"
    CST_CDT = "Central Time (CST or CDT)"
    EST_EDT = "Eastern Time (EST or EDT)"
    NST_NDT = "Newfoundland Time (NST or NDT)"
    AST_ADT = "Atlantic Time (AST or ADT)"

class Resume(BaseModel):
    profile_id: int
    name: str
    skills: List[str]
    specialization: Specialization
    location: Optional[str] 
    timezone: TimeZone
    position: Optional[str]
    about: str