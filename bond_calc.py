from dataclasses import dataclass

from bond import BondSpec


@dataclass
class BondYieldResult:
    total_return_usd: float
    profit_usd: float
    profit_percentage: float


def convert_currency(amount: float, rate: float) -> float:
    return amount * rate


def calculate_annual_coupon_payment(investment_uah: float, coupon_rate: float) -> float:
    return investment_uah * (coupon_rate / 100)


def calculate_total_coupon_payments(annual_coupon_payment: float, duration_years: float) -> float:
    return annual_coupon_payment * duration_years


def calculate_nominal_yield(investment_uah: float, nominal_yield_rate: float, duration_years: float) -> float:
    return investment_uah * (nominal_yield_rate / 100) * duration_years


def calculate_bond_yield(investment_usd: float, start_exchange_rate: float, end_exchange_rate: float, bond_spec: BondSpec) -> BondYieldResult:
    if investment_usd <= 0:
        raise ValueError("Investment amount must be a positive number.")

    investment_uah = convert_currency(investment_usd, start_exchange_rate)

    annual_coupon_payment = calculate_annual_coupon_payment(investment_uah, bond_spec.coupon_rate)
    total_coupon_payments = calculate_total_coupon_payments(annual_coupon_payment, bond_spec.duration_years)
    total_nominal_yield = calculate_nominal_yield(investment_uah, bond_spec.nominal_yield_rate, bond_spec.duration_years)

    total_return_uah = investment_uah + total_coupon_payments + total_nominal_yield
    total_return_usd = convert_currency(total_return_uah, 1 / end_exchange_rate)

    profit_usd = total_return_usd - investment_usd
    profit_percentage = (profit_usd / investment_usd) * 100

    return BondYieldResult(total_return_usd, profit_usd, profit_percentage)
