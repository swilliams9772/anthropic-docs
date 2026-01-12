# Purchasing and managing seats

**Source:** https://support.claude.com/en/articles/12004354-how-to-purchase-and-manage-premium-seats

Seat management is available for Team and Enterprise plans.

This guide covers how to purchase seats, adjust your plan's seat allocation, reassign users between seat types, and understand billing on Team and Enterprise plans.

**Permissions note:** Only Owners and Primary Owners can purchase seats and access [Admin settings > Billing](https://claude.ai/admin-settings/billing). Admins and above can reassign seat types for members in [Admin settings > Organization](https://claude.ai/admin-settings/organization).

For information on adding and removing members from your organization, see [Managing members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans).

---

# Understanding seat types

Team and Enterprise plans offer two types of seats:

* **Standard seats** include base features and usage limits. On Enterprise plans, this includes all [core Enterprise plan features](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan#h_ad7ae272d1).
* **Premium seats** include the core features above, plus access to Claude Code and higher usage limits.

Organizations can mix and match seat types, assigning premium seats to power users who need more usage or Claude Code access while keeping other team members on standard seats.

Your plan has a total seat allocation (e.g., 50 standard seats and 10 premium seats). Within that allocation, you can assign and reassign users to different seat types as needed.

---

# Purchasing seats

Use these steps to add seats to your plan's total allocation.

# Team plans

1. Log in with your Owner or Primary Owner account.
2. Navigate to [Admin settings > Organization](https://claude.ai/admin-settings/organization).
3. Click “Manage” under “Total seats.”
4. In the “Seat breakdown” modal, click “Add or change seats.”
5. Click the "**+**" next to the seat type you want to add (standard or premium).
6. Click “Next” to review your purchase details and confirm the billing impact.
7. Check the confirmation box before continuing.
8. Click “Confirm & purchase” to complete the transaction.

**Note:** You can also purchase seats while adding a new member. If you don't have an available seat of the selected type, you'll be prompted to purchase one.

# Enterprise plans (annual invoiced contracts)

1. Log in with your Owner or Primary Owner account.
2. Go to [Admin settings > Billing](https://claude.ai/admin-settings/billing).
3. Click the **pencil icon** under **Seats**.
4. Make any necessary seat increases.
5. Review your changes carefully before confirming.
6. Click “Upgrade” to finalize.

---

# Reducing your plan's seat allocation

# Team plans

You can reduce the total number of seats on your Team plan:

1. Log in with your Owner or Primary Owner account.
2. Navigate to [Admin settings > Organization](https://claude.ai/admin-settings/organization).
3. If needed, remove members or reassign them to free up the seats you want to eliminate.
4. Click “Manage” under **Total seats**.
5. Click “Add or change seats” in the **Seat breakdown** modal.
6. Click the "**-**" next to the seat type you want to reduce.
7. Click “Next” to review the changes.
8. Check the confirmation box and click "Confirm & purchase" to complete the change.

# Enterprise plans

Seats cannot be removed from your total allocation on Enterprise plans. However, you can reassign seats to different team members as needed. Contact your account manager if you need to discuss adjusting your seat allocation.

---

# Assigning and reassigning seat types

You can move users between standard and premium seats within your plan's existing allocation.

# How to reassign a user's seat type

1. Go to [Admin settings > Organization](https://claude.ai/admin-settings/organization).
2. Find the member you want to reassign.
3. Click the dropdown under **Seat Tier**.
4. Select the appropriate tier (standard or premium).

Members assigned to premium seats will automatically gain access to Claude Code and increased usage limits. Members moved from premium to standard will lose access to these features.

# Using "unassigned" to swap users between seat types

The unassigned tier is a placeholder that allows you to temporarily remove a user from a seat without removing them from your organization. This is useful when you need to swap people between seat types within your existing allocation.

**Example:** You have five premium seats, all assigned. You want to move User A (currently on premium) to standard, and move User B (currently on standard) to premium—without purchasing an additional seat.

1. Go to [Admin settings > Organization](https://claude.ai/admin-settings/organization).
2. Find User A and change their Seat Tier to "Unassigned." This frees up one premium seat.
3. Find User B and change their Seat Tier to "Premium." They now occupy the free premium seat.
4. Find User A and change their Seat Tier to "Standard."

**Note:** Unassigned users remain members of your organization but cannot use Claude until they're assigned to a seat tier.

# What if I don't have an available seat?

If you try to reassign a user to premium but don't have any available premium seats, you'll be prompted to purchase an additional premium seat.

# Differences between Team and Enterprise plans

* **Team plans:** You can freely reassign users between seat types. You can also reduce your total number of premium seats by reassigning users to standard and then reducing your plan's premium seat allocation.
* **Enterprise plans:** You can reassign users between seat types, but you cannot reduce your plan's total seat allocation. For example, if you have 10 premium seats and reassign some users to standard, those premium seats remain on your plan and available for future use.

# Seat assignment with JIT or SCIM provisioning

[Users provisioned via JIT or SCIM](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning-to-manage-user-assignments-on-team-or-enterprise-plans) are automatically assigned to the highest-available seat tier when they're added. Admins and above can manually reassign seat types afterward in [Admin settings > Organization](https://claude.ai/admin-settings/organization).

You can also use Advanced Group Mappings with JIT or SCIM to provision users directly to a specific seat tier.

---

# Understanding billing

# Team plans

* **New seats** are prorated based on your billing cycle and charged immediately.
* **Seat type changes** are also prorated when you reassign a user from standard to premium and subsequently purchase a new premium seat. In this case you'll be charged immediately for the price difference, prorated for the remainder of your billing cycle.
* **Removing members** does not trigger an immediate credit or refund. The seat becomes available to assign to another member. If you want to reduce your bill, you'll need to reduce your plan's total seat allocation.

For detailed billing calculations and examples, see [How is my Team plan bill calculated?](https://support.claude.com/en/articles/9267289-how-is-my-team-plan-bill-calculated)

# Enterprise plans (annual invoiced contracts)

* New seats are billed at your contract's existing per-user price.
* You receive an invoice immediately when new seats are added.
* Each new seat is prorated for the remainder of your annual term.
* For auto-renewal contracts, your renewal will include the total number of seats in use at the end of your term.

**Example:** If you start with 100 standard seats on January 1 and on March 1 you add 5 more standard seats and purchase 10 premium seats, you'll receive an invoice immediately for:

* The 5 additional standard seats (prorated for the 10 months remaining in the term)
* The 10 premium seats (prorated for the 10 months remaining)

For specific information about Enterprise pricing, reach out to your Account Manager or our [Sales team](https://claude.com/contact-sales).

---

Related Articles

[What is the Team plan?](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)[How is my Team plan bill calculated?](https://support.claude.com/en/articles/9267289-how-is-my-team-plan-bill-calculated)[Using Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)[Extra Usage for Team and Enterprise Plans](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-enterprise-plans)[Managing members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)
