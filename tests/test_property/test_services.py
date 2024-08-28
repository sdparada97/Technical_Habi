# Third party
import mysql.connector
import pytest

# First party
from app.db import config
from app.repositories.property_repository import Join, PropertyRepository
from app.schemas.property_schema import Status
from app.services.property_service import PropertyService

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

property_filters_data = [
    ({}, 0),
    ({'status': [Status.EN_VENTA.value], }, 0),
    ({'city': ['bogota'], }, 0),
    ({'year': ['2021'], }, 0),
    ({
        'status': [Status.EN_VENTA.value],
        'city': ['bogota'],
        'year': ['2021']
    }, 0)
]


@pytest.fixture
def repository():
    return PropertyRepository()


@pytest.fixture(scope="session")
def mysql_connection():
    connection = mysql.connector.connect(**config)
    yield connection
    connection.close()


@pytest.fixture(scope='session')
def mysql_cursor():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    yield cursor
    cursor.close()
    connection.close()


def test_mysql_connection(mysql_connection):
    assert mysql_connection.is_connected() is True


@pytest.mark.parametrize("params, expected", property_filters_data)
def test_get_all_with_filters(repository, params, expected):
    service = PropertyService(repository)
    result = service.get_all_with_filters(params)
    assert len(result) > expected
