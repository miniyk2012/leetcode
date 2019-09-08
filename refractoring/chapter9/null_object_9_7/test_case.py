from pytest import fixture

from refractoring.chapter9.null_object_9_7.null_object_after import (
    Site as SiteAfter,
    Customer as CustomerAfter,
    PaymentHistory as PaymentHistoryAfter)
from refractoring.chapter9.null_object_9_7.null_object_before import (
    Site as SiteBefore,
    Customer as CustomerBefore,
    PaymentHistory as PaymentHistoryBefore)


@fixture(scope="module")
def init_sites_after_refractor():
    site0 = SiteAfter()

    c1 = CustomerAfter("yangkai", None, None)
    site1 = SiteAfter(c1)

    payment_history = PaymentHistoryAfter(5)
    c2 = CustomerAfter("duxiaojian", "plan2", payment_history)
    site2 = SiteAfter(c2)
    return site0, site1, site2


@fixture(scope="module")
def init_sites_before_refractor():
    site0 = SiteBefore()

    c1 = CustomerBefore("yangkai", None, None)
    site1 = SiteBefore(c1)

    payment_history = PaymentHistoryBefore(5)
    c2 = CustomerBefore("duxiaojian", "plan2", payment_history)
    site2 = SiteBefore(c2)
    return site0, site1, site2


def test_before(init_sites_before_refractor):
    site0, site1, site2 = init_sites_before_refractor

    name0, plan0, weeks_delinquent0 = get_information_before(site0)
    assert name0 == "Unknown" and plan0 == "Basic Plan" and weeks_delinquent0 == 0

    name1, plan1, weeks_delinquent1 = get_information_before(site1)
    assert name1 == "yangkai" and plan1 == "Basic Plan" and weeks_delinquent1 == 0

    name2, plan2, weeks_delinquent2 = get_information_before(site2)
    assert name2 == "duxiaojian" and plan2 == "plan2" and weeks_delinquent2 == 5


def test_after(init_sites_after_refractor):
    site0, site1, site2 = init_sites_after_refractor

    name0, plan0, weeks_delinquent0 = get_information_after(site0)
    assert name0 == "Unknown" and plan0 == "Basic Plan" and weeks_delinquent0 == 0

    name1, plan1, weeks_delinquent1 = get_information_after(site1)
    assert name1 == "yangkai" and plan1 == "Basic Plan" and weeks_delinquent1 == 0

    name2, plan2, weeks_delinquent2 = get_information_after(site2)
    assert name2 == "duxiaojian" and plan2 == "plan2" and weeks_delinquent2 == 5


def get_information_before(site):
    c = site.customer
    if c is None:
        name = "Unknown"
        plan = "Basic Plan"
        weeks_delinquent = 0
    else:
        name = c.name or "Unkonwn"
        plan = c.plan or "Basic Plan"
        payment_history = c.payment_history
        if payment_history is None:
            weeks_delinquent = 0
        else:
            weeks_delinquent = payment_history.get_weeks_delinquent_in_last_year()
    return name, plan, weeks_delinquent


def get_information_after(site):
    """客户用起来方便多了"""
    c = site.customer
    name = c.name
    plan = c.plan
    weeks_delinquent = c.payment_history.get_weeks_delinquent_in_last_year()
    return name, plan, weeks_delinquent
