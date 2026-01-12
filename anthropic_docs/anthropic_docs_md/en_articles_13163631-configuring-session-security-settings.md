# Configuring session security settings

**Source:** https://support.claude.com/en/articles/13163631-configuring-session-security-settings

This feature is available to Admins and Owners of Enterprise plans and Console Admins.

Session duration controls allow Enterprise and Console Admins to set a maximum session length for all users in their organization. When enabled, users will need to sign in again after the specified period, even if they've been actively using Claude. This helps protect your organization by limiting how long a compromised session could remain valid.

# Enabling session length settings

# For Enterprise Admins

1. Log in to your Enterprise organization as an Admin or above.
2. Navigate to [Admin settings > Identity and access](https://claude.ai/admin-settings/identity).
3. Locate the **Session security** section.
4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 7 days, 14 days, or 28 days.
5. Confirm your selection by clicking “Enable.”

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469436/1725e63ea1a2615948faecf4ec73/9bd276a1-7329-414d-87a1-d04dac93fff7?expires=1767998700&signature=da43e075caf83f1cccf203e74addef2ffb9cefa3c5b342d0548465e480b0c02b&req=dSgvHs14lIVcX%2FMW1HO4zQNx5eUuSlJXg%2F6XaftFnjywgrUgeYUMBgnw0dme%0AgTXK%2FmYiuEUwEmLQrMo%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469436/1725e63ea1a2615948faecf4ec73/9bd276a1-7329-414d-87a1-d04dac93fff7?expires=1767998700&signature=da43e075caf83f1cccf203e74addef2ffb9cefa3c5b342d0548465e480b0c02b&req=dSgvHs14lIVcX%2FMW1HO4zQNx5eUuSlJXg%2F6XaftFnjywgrUgeYUMBgnw0dme%0AgTXK%2FmYiuEUwEmLQrMo%3D%0A)

# For Console Admins

1. Log in to your Console account as an Admin.
2. Navigate to [Settings > Identity and access](http://platform.claude.com/settings/identity).
3. Locate the **Session security** section.
4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 1 day, 3 days, or 7 days.
5. Confirm your selection by clicking “Enable.”

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469435/7a766bbe02e61c7d8f05deb5b8f0/b0bda400-47c6-43dd-9907-131ebe180b36?expires=1767998700&signature=043a053800a6e2d5a3c160a0e29f499744c0908de195eebd240a60c78e4e124e&req=dSgvHs14lIVcXPMW1HO4zWzx1r4%2FLncmXZ5D7eVpMtdGzZKSwFj%2BBN9GJ3NV%0A7JpTzX5afeeljNSdGyI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469435/7a766bbe02e61c7d8f05deb5b8f0/b0bda400-47c6-43dd-9907-131ebe180b36?expires=1767998700&signature=043a053800a6e2d5a3c160a0e29f499744c0908de195eebd240a60c78e4e124e&req=dSgvHs14lIVcXPMW1HO4zWzx1r4%2FLncmXZ5D7eVpMtdGzZKSwFj%2BBN9GJ3NV%0A7JpTzX5afeeljNSdGyI%3D%0A)

# What happens after enabling shortened session length?

* Existing sessions older than the selected duration will expire immediately.
* Other active sessions will expire no later than the selected duration.
* Users whose sessions expire will be directed to sign in again.

# Updating session duration

You can change the session duration at any time by selecting a new value from the dropdown. If you select a shorter duration:

* Sessions older than the new duration will expire immediately.
* Sessions scheduled to expire beyond the new duration will have their expiration shortened accordingly.

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469437/46ac5bc55484ca01556d87a5ade7/b01a7651-ad65-4b32-93ff-16dbc9ca97c0?expires=1767998700&signature=0554bb60a00edbe1b664d2a47e952fe512d489732347e39e0211816553654f3a&req=dSgvHs14lIVcXvMW1HO4zZ7mVM%2BS7jGkA00cbyPOLDUtSXw4FFq6APa8gARS%0A3xhLvbywXo7UPm0a7f8%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469437/46ac5bc55484ca01556d87a5ade7/b01a7651-ad65-4b32-93ff-16dbc9ca97c0?expires=1767998700&signature=0554bb60a00edbe1b664d2a47e952fe512d489732347e39e0211816553654f3a&req=dSgvHs14lIVcXvMW1HO4zZ7mVM%2BS7jGkA00cbyPOLDUtSXw4FFq6APa8gARS%0A3xhLvbywXo7UPm0a7f8%3D%0A)

# Disabling session length settings

To disable session duration, select "Disable" next to **Shortened session length**. Existing active sessions will continue to expire at their scheduled time. New sessions will return to default behavior, where sessions remain active as long as the user stays active.

# Users in multiple organizations

If a user belongs to multiple organizations with different session duration settings, the shortest duration will be applied. For example, if a user is a member of Organization A (7-day limit) and Organization B (28-day limit), their sessions will expire after seven days. This is because a single session is used across all their organizations, so the most restrictive setting takes precedence.

---

Related Articles

[Important Considerations Before Enabling Single Sign-On (SSO) and JIT/SCIM Provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)[Microsoft 365 Connector: Security Guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)[Setting up Single Sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)[Setting up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)[Managing members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)
