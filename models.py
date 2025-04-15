from pydantic import BaseModel, Field

class VehicleStatus(BaseModel):
    engine: str = Field(..., description="Engine status, e.g., 'on' or 'off'")
    battery_level: int = Field(..., ge=0, le=100, description="Battery percentage")
    fuel_level: int = Field(..., ge=0, le=100, description="Fuel percentage")
    warning_message: str = Field(..., description="System warning message")
