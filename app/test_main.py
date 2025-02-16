from unittest import mock
from app.main import outdated_products
import pytest
import datetime
import time_machine


@pytest.fixture
def mock_time_date():
    with mock.patch("datetime.date.today") as mock_dt:
        yield mock_dt

@pytest.mark.parametrize(
    "products,today,expired_product_names",
    [
        (
            [
                {
                    "name": "good product",
                    "expiration_date": datetime.date(2020, 1, 1)
                },
                {
                    "name": "expired product",
                    "expiration_date": datetime.date(2019, 12, 31)
                }
            ],
            datetime.date(2020, 1, 1),
            ["expired product"]
        ),
        (
            [
                {
                    "name": "good product",
                    "expiration_date": datetime.date(2045, 3, 3),
                },
                {
                    "name": "expired product",
                    "expiration_date": datetime.date(2045, 3, 2)
                },
                {
                    "name": "expired product",
                    "expiration_date": datetime.date(2045, 2, 2)
                }
            ],
            datetime.date(2045, 3, 3),
            ["expired product", "expired product"]
        )
    ]
)
def test_outdated_products_for_different_datetime_now(
        mock_dt,
        products: list,
        today: datetime.date,
        expired_product_names: list[str]
) -> None:
    mock_dt.return_value = today
    assert outdated_products(products) == expired_product_names


# @mock.patch("datetime.date.today")
# def test_outdated_products_for_different_datetime_now(mock_dt, products: list, today: datetime.date, expired_product_names: list[str]) -> None:
#     mock_dt.return_value = today
#     assert outdated_products(products) == expired_product_names
