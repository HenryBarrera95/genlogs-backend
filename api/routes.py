from fastapi import APIRouter, HTTPException

from api.schemas import CarriersResponse
from api.services import get_carriers_for_route


router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/carriers", response_model=CarriersResponse)
def carriers(from_city: str | None = None, to_city: str | None = None):
    if not from_city or not to_city:
        raise HTTPException(status_code=400, detail="from_city and to_city are required")

    carriers_list = get_carriers_for_route(from_city, to_city)
    return {"from_city": from_city, "to_city": to_city, "carriers": carriers_list}
