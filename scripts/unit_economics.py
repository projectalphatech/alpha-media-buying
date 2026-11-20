#!/usr/bin/env python3
"""Break-even and target acquisition costs for a lead -> prospect -> customer funnel.

'Prospect' = a lead that reaches your intermediate step (sample, demo, audit, quote).
If you have no such step, set --lead-to-prospect to your qualified rate and
--prospect-to-client to qualified -> paid.

Example:
  python unit_economics.py --revenue 25000 --margin 0.6 \
      --lead-to-prospect 0.4 --prospect-to-client 0.2 --free-step-cost 300

All money values are in one currency (whatever you pass in). Ad spend should
be counted including VAT and fees.
"""
import argparse


def compute(revenue, margin, lead_to_prospect, prospect_to_client,
            free_step_cost=0.0, sales_cost_per_client=0.0, spend_share=0.5,
            ltv_multiple=1.0):
    for name, rate in (("margin", margin), ("lead_to_prospect", lead_to_prospect),
                       ("prospect_to_client", prospect_to_client),
                       ("spend_share", spend_share)):
        if not 0 < rate <= 1:
            raise ValueError(f"{name} must be in (0, 1], got {rate}")

    gross_profit = revenue * margin * ltv_multiple
    lead_to_client = lead_to_prospect * prospect_to_client
    # A free step (sample, demo, audit) is delivered to every prospect, so each
    # customer carries the cost of the free steps that did not convert.
    free_step_cost_per_client = free_step_cost / prospect_to_client
    non_ad_cost = free_step_cost_per_client + sales_cost_per_client

    breakeven_ad_cac = gross_profit - non_ad_cost
    target_ad_cac = gross_profit * spend_share - non_ad_cost

    return {
        "gross_profit_per_client": gross_profit,
        "lead_to_client_rate": lead_to_client,
        "leads_per_client": 1 / lead_to_client,
        "non_ad_cost_per_client": non_ad_cost,
        "breakeven_ad_cac": breakeven_ad_cac,
        "target_ad_cac": target_ad_cac,
        "breakeven_cpl": breakeven_ad_cac * lead_to_client,
        "target_cpl": target_ad_cac * lead_to_client,
        "breakeven_cost_per_prospect": breakeven_ad_cac * prospect_to_client,
        "target_cost_per_prospect": target_ad_cac * prospect_to_client,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--revenue", type=float, required=True,
                   help="average first-project revenue per new client")
    p.add_argument("--margin", type=float, required=True,
                   help="gross margin after delivery cost, 0-1")
    p.add_argument("--lead-to-prospect", type=float, required=True,
                   help="share of leads that qualify and reach the free step (sample, demo, audit, quote), 0-1")
    p.add_argument("--prospect-to-client", type=float, required=True,
                   help="share of prospects that pay, 0-1")
    p.add_argument("--free-step-cost", type=float, default=0.0,
                   help="cost to deliver one free step (sample, demo, audit); 0 if none")
    p.add_argument("--sales-cost", type=float, default=0.0,
                   help="human sales time cost per closed client")
    p.add_argument("--spend-share", type=float, default=0.5,
                   help="share of gross profit you accept spending on acquisition (default 0.5)")
    p.add_argument("--ltv-multiple", type=float, default=1.0,
                   help="lifetime gross profit / first-project gross profit (default 1 = ignore repeat work)")
    a = p.parse_args()

    r = compute(a.revenue, a.margin, a.lead_to_prospect, a.prospect_to_client,
                a.free_step_cost, a.sales_cost, a.spend_share, a.ltv_multiple)

    print(f"Gross profit per client        {r['gross_profit_per_client']:>12,.0f}")
    print(f"Lead -> client rate            {r['lead_to_client_rate']:>12.1%}   ({r['leads_per_client']:.1f} leads per client)")
    print(f"Non-ad cost per client         {r['non_ad_cost_per_client']:>12,.0f}   (free steps + sales time)")
    print()
    print(f"{'':30} {'break-even':>12} {'target':>12}")
    print(f"{'Ad cost per client (CAC)':30} {r['breakeven_ad_cac']:>12,.0f} {r['target_ad_cac']:>12,.0f}")
    print(f"{'Cost per prospect':30} {r['breakeven_cost_per_prospect']:>12,.0f} {r['target_cost_per_prospect']:>12,.0f}")
    print(f"{'Cost per lead (CPL)':30} {r['breakeven_cpl']:>12,.0f} {r['target_cpl']:>12,.0f}")
    if r["target_ad_cac"] <= 0:
        print("\nTarget CAC is zero or negative: at these rates the offer cannot pay for ads.")
        print("Raise price or close rate, cut free-step cost, or count repeat revenue (--ltv-multiple).")


if __name__ == "__main__":
    main()
