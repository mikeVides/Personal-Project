from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column

class Base(MappedAsDataclass, DeclarativeBase):
    pass


class DataCollected(Base):
    __tablename__ = 'data_collected'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Employee_ID: Mapped[Optional[str]] = mapped_column(String(255))
    Age: Mapped[Optional[int]] = mapped_column(Integer)
    Gender: Mapped[Optional[str]] = mapped_column(String(255))
    Job_Role: Mapped[Optional[str]] = mapped_column(String(255))
    Industry: Mapped[Optional[str]] = mapped_column(String(255))
    Years_of_Experience: Mapped[Optional[int]] = mapped_column(Integer)
    Work_Location: Mapped[Optional[str]] = mapped_column(String(255))
    Hours_Worked_Per_Week: Mapped[Optional[int]] = mapped_column(Integer)
    Number_of_Virtual_Meetings: Mapped[Optional[int]] = mapped_column(Integer)
    Work_Life_Balance_Rating: Mapped[Optional[int]] = mapped_column(Integer)
    Stress_Level: Mapped[Optional[str]] = mapped_column(String(255))
    Mental_Health_Condition: Mapped[Optional[str]] = mapped_column(String(255))
    Access_to_Mental_Health_Resources: Mapped[Optional[str]] = mapped_column(String(255))
    Productivity_Change: Mapped[Optional[str]] = mapped_column(String(255))
    Social_Isolation_Rating: Mapped[Optional[int]] = mapped_column(Integer)
    Satisfaction_with_Remote_Work: Mapped[Optional[str]] = mapped_column(String(255))
    Company_Support_for_Remote_Work: Mapped[Optional[int]] = mapped_column(Integer)
    Physical_Activity: Mapped[Optional[str]] = mapped_column(String(255))
    Sleep_Quality: Mapped[Optional[str]] = mapped_column(String(255))
    Region: Mapped[Optional[str]] = mapped_column(String(255))
