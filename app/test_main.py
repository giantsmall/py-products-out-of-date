from app.main import outdated_products
import pytest
import datetime
import time_machine


@pytest.mark.parametrize(
    "products,mock_today,expired_product_names",
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
        products: list,
        mock_today: datetime.date,
        expired_product_names: list[str]
) -> None:
    with time_machine.travel(mock_today):
        assert outdated_products(products) == expired_product_names
