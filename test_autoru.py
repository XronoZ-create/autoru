from autoru import total_count, marks, mark_models

# a = total_count(proxy='http://giachnCnYW:uv0ihnpGrN@193.58.170.206:45746', headless=False)

# a = marks(proxy='http://giachnCnYW:uv0ihnpGrN@193.58.170.206:45746', headless=False)

# a = mark_models(proxy='http://giachnCnYW:uv0ihnpGrN@193.58.170.206:45746', headless=False)

a = mark_models(proxy='http://giachnCnYW:uv0ihnpGrN@193.58.170.206:45746',
                headless=False, mark_model_url='https://auto.ru/moskva/cars/ac/all/')

print(a)
