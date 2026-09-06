"""Forward Rate Agreement (FRA) settlement calculator.

Asks for the four terms of an FRA, then reports who pays whom at settlement.
"""


def main():
    print("FRA Settlement Calculator")
    print("-" * 25)

    # Ask the user for each term. input() always hands back text, so we
    # convert: float() for numbers that can have decimals, int() for whole days.
    notional = float(input("Notional amount: "))
    fra_rate = float(input("Locked-in FRA rate (%): "))
    days = int(input("Number of days: "))
    market_rate = float(input("Market rate at settlement (%): "))

    # Rates were typed as percentages (5.25), so divide by 100 to get the
    # decimal form (0.0525) that the formula needs.
    rate_difference = (market_rate - fra_rate) / 100

    # The settlement formula: (market rate - FRA rate) x notional x days/360.
    # 360 is the day-count convention used for most money-market rates.
    payment = rate_difference * notional * (days / 360)

    print()
    print(f"Rate difference: {market_rate - fra_rate:+.4f}%")

    # A positive payment means rates rose above the locked-in rate, so the
    # seller compensates the buyer. Negative means the reverse.
    if payment > 0:
        print(f"The seller pays the buyer: {payment:,.2f}")
    elif payment < 0:
        print(f"The buyer pays the seller: {abs(payment):,.2f}")
    else:
        print("Rates match exactly - no payment is owed.")


# This line means: only run main() when the file is executed directly
# (python3 fra_calculator.py), not when it is imported by another file.
if __name__ == "__main__":
    main()
