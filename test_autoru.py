from autoru import total_count, marks, mark_models

a = total_count(
    proxy_id=None, proxy_ip=None, proxy_port=None,
    proxy_login=None, proxy_pwd=None, proxy_type='https',
    headless=False
)

# a = marks(
#     proxy_id=None, proxy_ip=None, proxy_port=None,
#     proxy_login=None, proxy_pwd=None, proxy_type='no_proxy',
#     headless=False
# )

# a = mark_models(
#     proxy_id=None, proxy_ip=None, proxy_port=None,
#     proxy_login=None, proxy_pwd=None, proxy_type='no_proxy',
#     headless=False, mark_model_url='https://auto.ru/moskva/cars/audi/all/'
# )

# a = mark_models(
#     proxy_id=None, proxy_ip=None, proxy_port=None,
#     proxy_login=None, proxy_pwd=None, proxy_type='no_proxy',
#     headless=False, mark_model_url='https://auto.ru/moskva/cars/ac/all/'
# )

print(a)
