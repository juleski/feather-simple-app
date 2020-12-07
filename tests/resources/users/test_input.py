complete_data = {
    "email": "pakler@email.com",
    "firstname": "test",
    "address": "Metro Manila",
    "occupation": "employed",
    "has_child": True,
    "child_num": 3,
}

data_without_email = complete_data.copy()
data_without_email.pop("email", None)

data_without_firstname = complete_data.copy()
data_without_firstname.pop("firstname", None)

data_without_address = complete_data.copy()
data_without_address.pop("address", None)

data_without_occupation = complete_data.copy()
data_without_occupation.pop("occupation", None)

data_without_has_child = complete_data.copy()
data_without_has_child.pop("has_child", None)
data_without_has_child.pop("child_num", None)
