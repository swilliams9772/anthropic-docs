# Setting up JIT or SCIM provisioning

**Source:** https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning-to-manage-user-assignments-on-team-or-enterprise-plans

JIT provisioning is available for Team plans, Enterprise plans, and Console organizations. SCIM provisioning is available for Enterprise and Console organizations only.

This guide covers how to configure user provisioning and role assignment for your Claude or Claude Console organization.

**Before you begin:** This guide assumes you have already completed the steps in [Setting up Single Sign-On (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso-for-claude-and-claude-console), including domain verification and SSO configuration with your Identity Provider (IdP), and you have an Admin (Console) or Owner (Claude) role.

# Step 1: Choose your provisioning mode

Once SSO is configured, you need to decide how users will be provisioned to your organization. This is controlled by the **Provisioning mode** setting in your Identity and access settings.

# Provisioning options

**Manual** is the default. Users are added and removed directly in Claude or Console settings.

**JIT (Just-in-Time):** Users assigned to your Anthropic IdP app are automatically provisioned when they first log in. This option is available to all plans.

**SCIM:** Users are automatically provisioned and deprovisioned based on assignments in your IdP, without requiring them to log in first. SCIM is available for Enterprise plans and Console organizations with their own parent organization or joined to an Enterprise parent organization. SCIM is not available for Team plans or Console organizations joined to a Team plan's parent organization.

# Provisioning behavior overview

Use this table to help decide which provisioning mode is right for your organization:

|  |  |  |  |
| --- | --- | --- | --- |
| **Mode** | **Provisioning** | **Role and seat tier changes** | **Removal** |
| Manual | Users are manually added | Roles and seat tiers are manually changed | Users are manually removed |
| JIT | Users assigned to your IdP app are provisioned at login with the User role | Roles and seat tiers are manually changed | Manual removal required: users removed from your IdP app can no longer log in, but remain in the user list until they attempt to log in or are removed |
| JIT + advanced group mappings | Users in at least one mapped group are provisioned at login with the highest-permissioned role from their group memberships | Roles and seat tiers update on next login based on group membership | Users without group access can't log in but remain in the list until login attempt or manual removal |
| SCIM | Users assigned to your IdP app are automatically provisioned to all organizations joined to your parent org. | Roles and seat tiers are manually changed | Users removed from your IdP app are automatically removed |
| SCIM + advanced group mappings | Users in at least one mapped group are automatically provisioned with appropriate roles | Role and seat tier changes automatically propagate based on group membership | Automatic removal when group access is revoked |

Both JIT and SCIM can be combined with **Advanced Group Mappings** to control role or seat tier assignment based on IdP group membership.

# Available roles and seat tiers

|  |  |  |
| --- | --- | --- |
| **Product** | **Roles** | **Seat tiers** |
| Claude (Team/Enterprise) | Owner, Admin, User | Premium, Standard |
| Console | Admin, Developer, Billing, Claude Code User, User | — |

For detailed instructions on adding and removing members, see [Purchasing and managing seats](https://support.claude.com/en/articles/12004354-how-to-purchase-and-manage-premium-seats).

# Step 2: Set up SCIM directory sync (if using SCIM)

**Note:** Skip this step if you're using Manual or JIT provisioning.

If you chose SCIM as your provisioning mode, you need to establish the connection between your Identity Provider and Anthropic before enabling it.

1. Navigate to your Identity and access settings in Claude **(**[claude.ai/admin-settings/identity](http://claude.ai/admin-settings/identity)) or Console ([platform.claude.com/settings/identity](http://platform.claude.com/settings/identit))
2. In the “Global SSO Configuration” section, click “Setup SCIM” (or “Manage SCIM”**)** next to "Directory sync (SCIM)."
3. Follow the WorkOS setup guide to configure SCIM in your Identity Provider. You'll need to copy values from WorkOS into your IdP's Anthropic application.

**‼️When you reach the IdP Group step, pause to review Steps 3 and 4 of this guide, alongside the other guides.**

For IdP-specific JIT / SCIM setup instructions, see:

* [Okta SAML](https://workos.com/docs/integrations/okta-saml) / [OKTA SCIM](https://workos.com/docs/integrations/okta-scim)
* [Entra ID SAML](https://workos.com/docs/integrations/entra-id-saml) / [Entra ID SCIM](https://workos.com/docs/integrations/entra-id-scim)
* [Google SAML](https://workos.com/docs/integrations/google-saml) / [Directory Sync](https://workos.com/docs/integrations/google-directory-sync)
* [OneLogin SAML](https://workos.com/docs/integrations/onelogin-saml) / [OneLogin SCIM](https://workos.com/docs/integrations/onelogin-scim)
* [JumpCloud SAML](https://workos.com/docs/integrations/jumpcloud-saml) / [JumpCloud SCIM](https://workos.com/docs/integrations/jumpcloud-scim)
* See additional IdPs [here](https://workos.com/docs/integrations)

Once your IdP is connected, continue to Step 3.

# Step 3: Configure provisioning mode and Advanced Group Mappings

1. In the **Organization SSO Configuration** section of your Identity and access settings, find **Provisioning mode**.
2. Select your chosen option from the dropdown (“Just in time (JIT)” or “Directory sync (SCIM)”).
3. **If using Advanced Group Mappings:** Toggle on **Advanced group mappings** and note the organization ID 8-character prefix shown (e.g., anthropic-claudeai-[org-id] for Claude or anthropic-console-[org-id] for Console). You'll use this prefix to create groups for role mapping and, for Claude organizations, seat tier mapping.

   1. **Important:** Do NOT click “Save changes” yet. You must first ensure all users are assigned to your Anthropic application in your IdP. For Advanced Group Mappings, users must also be assigned to the appropriate groups (Steps 4 and 5). Saving before users are properly assigned will result in those users being deprovisioned from the organization.
4. **If you are not using Advanced Group Mappings:** Ensure all users are assigned to your Anthropic application in your IdP for SCIM provisioning, then click “Save changes” to complete your setup.

# Step 4: Configure groups and assign users in your Identity Provider for Advanced Group Mappings

1. Create groups in your IdP for each role and seat tier you want to assign.

   1. Group names must start with anthropic-claudeai-[org-id]- (for Claude) or anthropic-console-[org-id]- (for Console), followed by whatever you like (e.g., anthropic-claudeai-a1b2c3d4-sales).
   2. You can find the 8-character prefix in the “Advanced group mappings” section, or by copying the first eight characters of your org ID from [Admin settings > Organization](https://claude.ai/admin-settings/organization).
2. Ensure your IdP is configured to share groups with this prefix.
3. Add users to the groups you created, ensuring at least one user (including yourself) is in a group that will be mapped to an Admin (Console) or Owner (Claude) role.

**Important:** All users who need access must be assigned to the appropriate groups before you save your Advanced Group Mappings configuration in the next step. These users should already be assigned to your Anthropic application in your IdP from when you enabled SSO.

# Step 5: Map groups to roles and seat tiers

1. Return to your Identity and access settings in Claude or Console, and toggle **Advanced group mappings** on (if it’s not already).
2. In the **Role mappings** section, click “Add” next to each role and select the corresponding group from your IdP in the dropdown.
3. For Claude organizations: In the **Seat tier mappings** section, click “Add” next to each tier (Premium, Standard) and select the corresponding group. If a user isn't assigned to a seat tier group, they will be assigned to the highest available tier by default.
4. Verify all necessary groups are mapped to the appropriate roles and seat tiers.
5. Click “Save changes.”

**Note:** Microsoft Entra only pushes SCIM changes every 40 minutes, so there may be a delay before changes appear.

# Troubleshooting

# Users assigned correctly and showing in the directory but aren’t being added to the Claude as members?

Verify you have enough seats purchased and available to add members to your org.

1. Check “Total seats” shown on the Organization page, if needed, [purchase additional seats](https://support.claude.com/en/articles/12004354-how-to-purchase-and-manage-premium-seats).
2. Once you have available seats, go back to the Identity and access page and click “Sync now,” next to **Directory sync (SCIM)**. This will trigger a sync to provision accounts for those users not yet added as members.

# Users aren't being provisioned with the correct role

1. Verify the user is assigned to the correct group in your IdP.
2. Verify the group is mapped to the correct role in your Identity and access settings.
3. **For JIT:** The user needs to log out and log back in for role changes to take effect.
4. **For SCIM:** Click "Sync Now" to prompt an immediate sync, or wait for the automatic sync cycle.

# I lost Admin/Owner access after enabling Advanced Group Mappings

This happens when the person configuring Advanced Group Mappings isn't assigned to a group mapped to an Admin or Owner role, causing their permissions to be downgraded to User. To fix this:

**Option 1: Have another Admin/Owner reinstate your role**

1. Contact another Admin or Owner of your organization.
2. Ask them to navigate to [Admin settings > Organization](https://claude.ai/admin-settings/organization) (for Claude) or [Settings > Members](https://platform.claude.com/settings/members) (for Console).
3. Have them change your role back to Admin or Owner.

**Option 2: Fix via your Identity Provider**

1. In your IdP, assign yourself to a group with the correct prefix that maps to an Admin or Owner role.
2. **For JIT:** Log out and log back in to regain access.
3. **For SCIM:** Ask another Admin or Owner to click "Sync Now" in the Identity and access settings, or wait for the automatic sync cycle.

---

Related Articles

[What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)[Important Considerations Before Enabling Single Sign-On (SSO) and JIT/SCIM Provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)[Purchasing and managing seats](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)[Setting up Single Sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)[Managing members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)
