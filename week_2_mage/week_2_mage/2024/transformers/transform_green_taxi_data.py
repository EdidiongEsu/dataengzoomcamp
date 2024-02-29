if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    - Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero.
    - Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    - Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        transformed dataframe
    """
    # clean column names, make all lowercase and convert to snake_case
    data.columns = (data.columns
                    .str.replace(" ", "_")
                    .str.lower())


    # create new column of date dtype for 'lpep_pickup_date' from 'lpep_pickup_datetime'
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data['lpep_dropoff_date'] = data['lpep_dropoff_datetime'].dt.date


    # drop records of rides with no passengers
    # print(f"Rows with out passengers: {data['passenger_count'].fillna(0).isin([0]).sum() }")
    # data = data[data['passenger_count'] > 0]

    # drop records of rides with 0 trip_distance
    # print(f"Rows with 0 trip_distance: {data['trip_distance'].fillna(0).isin([0]).sum() }")
    # data = data[data['trip_distance'] > 0]

    return data