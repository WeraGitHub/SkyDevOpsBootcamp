def print_vat_with_keyword_params(**kwargs):
    print(kwargs)
    print(f"{vatpc:2.5}")


print_vat_with_keyword_params(vatpc=20, gross=1, message='Summary: ')
