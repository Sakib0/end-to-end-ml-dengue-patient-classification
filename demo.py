from dengue_classification.exception import CustomException
import sys



try:
    r=3/0
except Exception as e:
    raise CustomException(e, sys)
