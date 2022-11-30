from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit

def cm_not_null_count(self, col_name):
    return self.filter(col(col_name).isNotNull()).count()
  
def cm_currency_conversion(self, to_convert, column_name):
    """
    Converts currency by adding a new column to the dataframe.
    Params:
    to_convert: Name of the column for converting
    column_name: New column that contains converted values
    
    Examples
    --------
    >>> df.cm_currency_conversion('value','value_converted').show()
    +--------+-----+---------------+
    |Material|value|value_converted|
    +--------+-----+---------------+
    |       A|   50|          100.0|
    |       B|  100|          200.0|
    +--------+-----+---------------+
    """
    conversion_value = 2
    return self.withColumn(column_name, col(to_convert) * conversion_value)

DataFrame.cm_not_null_count = cm_not_null_count
DataFrame.cm_currency_conversion = cm_currency_conversion
