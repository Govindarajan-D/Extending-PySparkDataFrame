from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit

def not_null_count(self, col_name):
    return DataFrame(self._jdf, self.sql_ctx).filter(col(col_name).isNotNull()).count()
  
def currency_conversion(self, to_convert, column_name):
    # We can get this from another table or API
    conversion_value = 1.05
    df = DataFrame(self._jdf, self.sql_ctx)
    return df.withColumn(column_name, col(to_convert) * conversion_value)

DataFrame.not_null_count = not_null_count
DataFrame.currency_conversion = currency_conversion