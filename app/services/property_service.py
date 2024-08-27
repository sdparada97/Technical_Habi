# Third party
from toolz.dicttoolz import merge

# First party
from app.repositories.property_repository import Join, PropertyRepository


class PropertyService:
    def __init__(self, repository):
        self._repository: PropertyRepository = repository

    def get_all_with_filters(self, body_params):

        fields = ["p.address", "p.city", "p.price", "p.description", "s.name AS status"]

        joins = [
            Join(table="status_history sh", condition="p.id = sh.property_id"),
            Join(table="status s", condition="sh.status_id = s.id"),
            Join(
                table="""(
                    SELECT property_id, MAX(update_date) AS max_date
                    FROM status_history
                    GROUP BY property_id
                ) latest_status """,
                condition="sh.property_id = latest_status.property_id AND sh.update_date = latest_status.max_date",
            ),
        ]

        params = self._add_params_to_query(body_params)

        return self._repository.get_all_with_filters(
            fields=fields, joins=joins, params=params
        )

    def _add_params_to_query(self, params):
        status = {
            "s.id": (
                "(3,4,5)"
                if params.get("status") is None
                else f'({",".join(str(params.get("status")[0]))})'
            )
        }

        city = {
            "p.city": (
                None
                if params.get("city") is None
                else f"""('{"','".join(params.get('city'))}')"""
            )
        }

        year = {
            "YEAR(latest_status.max_date)": (
                None
                if params.get("year") is None
                else f'({",".join(params.get("year"))})'
            )
        }

        params_query = merge(status, city, year)
        return " AND ".join(
            f"{k} in {v}" for k, v in params_query.items() if v is not None
        )
