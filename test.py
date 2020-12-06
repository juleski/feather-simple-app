from feather_simple_api.resources.providers.provider import Provider
from feather_simple_api import db

p = Provider(
    name="Job Insurance",
    price=30.5,
    billing_period="per month",
    for_occupation="employed",
)
db.session.add(p)

p = Provider(
    name="Life Insurance",
    price=29.5,
    billing_period="per month",
    for_occupation="employed",
)
db.session.add(p)

p = Provider(
    name="Life Insurance",
    price=8.95,
    billing_period="per month",
    for_occupation="employed",
)
db.session.add(p)

p = Provider(
    name="Personal Liability",
    price=7.45,
    billing_period="per month",
    for_occupation="employed",
)
db.session.add(p)

p = Provider(
    name="Personal Liability",
    price=19.35,
    billing_period="per month",
    for_occupation="employed",
)
db.session.add(p)

p = Provider(
    name="Car", price=17.95, billing_period="per month", for_occupation="employed"
)
db.session.add(p)

p = Provider(
    name="Car", price=17.95, billing_period="per month", for_occupation="employed"
)
db.session.add(p)


p = Provider(
    name="Health (private)",
    price=32.5,
    billing_period="per month",
    for_occupation="employed",
)
db.session.add(p)

p = Provider(
    name="Health (private)",
    price=32.5,
    billing_period="per month",
    for_occupation="self-employed",
)
db.session.add(p)

p = Provider(
    name="Personal Liability",
    price=31.42,
    billing_period="per month",
    for_occupation="self-employed",
)
db.session.add(p)

p = Provider(
    name="Personal Liability",
    price=9.45,
    billing_period="per month",
    for_occupation="self-employed",
)
db.session.add(p)

p = Provider(
    name="Personal Liability",
    price=16.45,
    billing_period="per month",
    for_occupation="self-employed",
)
db.session.add(p)

p = Provider(
    name="Car", price=19.25, billing_period="per month", for_occupation="self-employed"
)
db.session.add(p)

p = Provider(
    name="Car", price=32.5, billing_period="per month", for_occupation="self-employed"
)
db.session.add(p)

p = Provider(
    name="Personal Liability",
    price=28.5,
    billing_period="per month",
    for_occupation="student",
)
db.session.add(p)

p = Provider(
    name="Life insurance",
    price=19.5,
    billing_period="per month",
    for_occupation="student",
)
db.session.add(p)

p = Provider(
    name="Job insurance",
    price=31.5,
    billing_period="per month",
    for_occupation="student",
)
db.session.add(p)

p = Provider(
    name="Personal Liability",
    price=19.5,
    billing_period="per month",
    for_occupation="student",
)
db.session.add(p)

p = Provider(
    name="Life insurance",
    price=8.95,
    billing_period="per month",
    for_occupation="student",
)
db.session.add(p)

p = Provider(
    name="Health (private)",
    price=7.45,
    billing_period="per month",
    for_occupation="student",
)
db.session.add(p)

db.session.commit()
