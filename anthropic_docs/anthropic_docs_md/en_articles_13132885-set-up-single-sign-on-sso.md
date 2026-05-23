# Set up single sign

**Source:** https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso

Single sign-on is available for Team plans, Enterprise plans, and Console organizations.

This guide covers the steps to configure SSO for Team and Enterprise plans, and Claude Console organizations.

# Step 1: Review prerequisites and important considerations

Before proceeding with SSO setup, complete the following:

**Review the considerations guide:** Read **[Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)** to understand parent organizations, determine your setup path, and complete any prerequisite steps such as merging organizations.

**Confirm you have the required role:**

* For Team or Enterprise plans: You must be an Owner or Primary Owner
* For Claude Console: You must be an Admin

**Confirm you have access to the following:**

* DNS settings for your company's email address domain
* Your company's SSO Identity Provider (IdP) used to log in to third-party applications (e.g., Okta, Google Workspace, etc.)

Please contact your organization's IT Administrator if you do not have permissions to manage Claude or company DNS settings.

**Note:** WorkOS is Anthropic's provider for domain verification and SSO setup. More details can be found in **[Anthropic's Subprocessor List](https://trust.anthropic.com/subprocessors)**. You will be taken through a WorkOS setup flow when configuring SSO and provisioning features – find your Identity Provider in their **[Integration documentation](https://workos.com/docs/integrations)**.

---

# Step 2: Verify your domain(s)

Domain verification proves that you own your company's domain. Once verified, you can configure SSO for accounts with your company's domain.

You can verify multiple domains for a single organization, but all domains must be managed through a single IdP. We don't support verifying domains from separate IdPs within the same organization.

**Note:** Verifying your domain by itself will not impact existing users' ability to access our products. End users’ access is only affected once SSO is set up and explicitly enforced.

1. Navigate to your **Organization and access** settings in Claude (**[claude.ai/admin-settings/organization](http://claude.ai/admin-settings/organization)**) or your **Identity and access** settings in Console (**[platform.claude.com/settings/identity](http://platform.claude.com/settings/identity)**) – note this page will only appear on Console if you've worked with Sales to enable SSO or completed a merge proposal.
2. In the **Domains** section, click “Add or edit domains.”
3. Enter the domain(s) you want to verify in the **Update organization email domains** modal and click the “+” button:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047041551/518afbae9c8011a6e3c98ffb651d/d2491145-362d-490b-bdcf-66a0a7656ddc?expires=1779557400&signature=c837087a57a164fe0183d284d8b1be692a130be8a7e90f28d1cdccb4cbba32de&req=diAjEcl6nIRaWPMW1HO4zQCfASSZi4rjs0%2B6T5c8FJ8RRC8b5k6AvtpFRCeM%0AknFD%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047041551/518afbae9c8011a6e3c98ffb651d/d2491145-362d-490b-bdcf-66a0a7656ddc?expires=1779557400&signature=c837087a57a164fe0183d284d8b1be692a130be8a7e90f28d1cdccb4cbba32de&req=diAjEcl6nIRaWPMW1HO4zQCfASSZi4rjs0%2B6T5c8FJ8RRC8b5k6AvtpFRCeM%0AknFD%0A)
4. Click “Save” when you’re finished adding domains.
5. The domain(s) you added will now appear in the **Domains** section; click “Verify” to the right of the domain(s) to begin the verification process.
6. Enter your domain in the text box and click “Continue”:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047042630/0617a562cd28a7ff0e607d66a30b/6bd08e1d-2b65-40ab-bc79-a257153854c1?expires=1779557400&signature=3a40fd51c1b79b20cb4f19be8dd6d834d195cd045c3db439cb77eba50cfa5e79&req=diAjEcl6n4dcWfMW1HO4zWHcuhSSktauyoyXAW0OlXpe%2FgsO7EjO6QnUlfp5%0AmAdF%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047042630/0617a562cd28a7ff0e607d66a30b/6bd08e1d-2b65-40ab-bc79-a257153854c1?expires=1779557400&signature=3a40fd51c1b79b20cb4f19be8dd6d834d195cd045c3db439cb77eba50cfa5e79&req=diAjEcl6n4dcWfMW1HO4zWHcuhSSktauyoyXAW0OlXpe%2FgsO7EjO6QnUlfp5%0AmAdF%0A)
7. This will generate a TXT record. Follow the instructions to add this TXT record to your domain provider.

   * If using a subdomain (e.g., subdomain.yourcompany.com), set your TXT record on that subdomain (e.g., \_acme-challenge.subdomain.yourco. mpany.com).
8. Wait 10 minutes for your DNS change to propagate.

   * *Note: DNS changes can take 24-48 hours to propagate globally.*
9. When you see the green "Verified" badge, you can close the instructions page.
10. If your domain shows as "Pending," use the "Refresh" button.

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047044496/b8df54a0331784cc9ae8f00112aa/bf9609c1-dc93-4665-a066-4cae2fe4b002?expires=1779557400&signature=f20d9776c4d572c81fdaf0d171f2b63c5d776e3b485b008184fb94bc8b50b68a&req=diAjEcl6mYVWX%2FMW1HO4zVjmViAFanO9PM2D8Zcdgrjus7rECFo5pOPP4weD%0AM9df%2F%2B0dLvYiulTqUCI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047044496/b8df54a0331784cc9ae8f00112aa/bf9609c1-dc93-4665-a066-4cae2fe4b002?expires=1779557400&signature=f20d9776c4d572c81fdaf0d171f2b63c5d776e3b485b008184fb94bc8b50b68a&req=diAjEcl6mYVWX%2FMW1HO4zVjmViAFanO9PM2D8Zcdgrjus7rECFo5pOPP4weD%0AM9df%2F%2B0dLvYiulTqUCI%3D%0A)

**Note:** Once your domain is verified, you'll see a **Restrict organization creation** toggle under **Security** on the Organization and access organization settings page. Enable this if you want to prevent users from creating new Claude or Console organizations—including personal accounts—using your verified domains.

---

# Step 3: Set up SSO with your Identity Provider

1. Navigate to your **Organization and access** settings in Claude (**[claude.ai/admin-settings/organization](http://claude.ai/admin-settings/organization)**) or your **Identity and access** settings in Console (**[platform.claude.com/settings/identity](http://platform.claude.com/settings/identity)**).
2. In the **Authentication** section, click “Setup SSO” (or “Manage SSO”).
3. Follow the setup guide provided for your Identity Provider (see below for additional guides).
4. At the end of these steps, you’ll be prompted to Test Single Sign-on to confirm there are no errors and the configuration is successful.
5. Once complete, navigate back to the **Organization and access** settings page for further configuration options.

**Important:** SSO enforcement might result in users being unable to log in if they are not correctly assigned to the Anthropic app in the IdP. If you have more than one Claude/Console org connected to your “parent org,” you will want to consider creating a unique IdP Group for each. For more information, see **[enable group mappings](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning#h_adee31eeba)**.

For IdP-specific setup instructions, see:

* **[Okta SAML](https://workos.com/docs/integrations/okta-saml)**
* **[Entra ID SAML (formerly Azure AD)](https://workos.com/docs/integrations/entra-id-saml)**
* **[Google SAML](https://workos.com/docs/integrations/google-saml)**
* **[OneLogin SAML](https://workos.com/docs/integrations/onelogin-saml)**
* **[JumpCloud SAML](https://workos.com/docs/integrations/jumpcloud-saml)**
* **[Duo SAML](https://workos.com/docs/integrations/duo-saml/4-enter-duo-saml-settings-in-your-workos-dashboard)**

---

# Step 4: Choose to require SSO

You can now choose to toggle on **Require SSO for Console** and/or **Require SSO for Claude,** on the **Organization and access** page, under the **Authentication** section:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312690200/bd2403586d4f6651ccd79e2a45af/b9f8d7ce-0def-49d9-bfb2-3a14352d7214?expires=1779557400&signature=561ba47a7fc67a6244246adea6bcd7b79ea39a12e809e9aba8003e40224a4218&req=diMmFM93nYNfWfMW1HO4zdAIBAakB3sOItXtKivx6ZGG4gnQx7LERiOl%2F3ze%0AFoj9eoYX7S3sKSxKMBM%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312690200/bd2403586d4f6651ccd79e2a45af/b9f8d7ce-0def-49d9-bfb2-3a14352d7214?expires=1779557400&signature=561ba47a7fc67a6244246adea6bcd7b79ea39a12e809e9aba8003e40224a4218&req=diMmFM93nYNfWfMW1HO4zdAIBAakB3sOItXtKivx6ZGG4gnQx7LERiOl%2F3ze%0AFoj9eoYX7S3sKSxKMBM%3D%0A)

When SSO is required, users must use the “Continue with SSO” option to log in to their Claude/Console accounts. When SSO is not required, they will have the option to choose “Continue with SSO” or “Continue with email.”

Before you decide, review **[What happens to existing users when SSO is enabled](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning#h_644f467167)**.

---

# Step 5: Choose your provisioning approach

Once SSO is enabled, you need to decide how users will be added to your organization by choosing an option within the **User provisioning** section of your **Organization and access** settings.

**Invite only** is the default. Users are added and removed directly in your Claude or Console settings. Please see **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)**.

**Just-in-Time (JIT) provisioning** can be enabled to automatically provision users when they first log in. By default, users assigned to your Anthropic IdP app first login, they will receive the User role. This is the simplest automated option and requires no additional configuration beyond selecting "Just-in-Time (JIT)" as your provisioning mode.

# Enable group mappings - when to configure additional provisioning features

For more control over provisioning, see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)**. You'll want to review this guide if you need to:

* Automatically assign roles or seat tiers based on IdP group membership.
* Use SCIM directory sync for automatic provisioning and deprovisioning.
* Manage access across multiple organizations (e.g., if you have both a Team/Enterprise organization and a Console organization linked to the same parent and need to control which users are provisioned to each).

**Note:** We don't currently support IdP-initiated login for Claude Console organizations that share SSO settings with a Team or Enterprise plan organization. Users will be redirected to claude.ai with IdP-initiated login. As a workaround, if possible in your IdP, create a bookmark called "Claude Console" that links to platform.claude.com/login?sso=true to redirect users to Console for SP-initiated login.

---

# Updating your SSO certificate

When your Identity Provider's X.509 signing certificate expires or is rotated, you'll need to update it in Claude or Console to maintain SSO functionality.

1. Navigate to your settings:

   * For Team and Enterprise plans: **[claude.ai/admin-settings/organization](http://claude.ai/admin-settings/organization)**
   * For Claude Console: **[platform.claude.com/settings/identity](http://platform.claude.com/settings/organization)**
2. In the **Authentication** section, click “Manage SSO.”
3. Find the **Metadata configuration** section and click “Edit.”
4. Update your certificate information and save your changes.
5. Click "Test sign-in" on the same page to confirm everything is working.

---

# Turning off SSO

You can toggle **Require SSO for Claude** or **Require SSO for Console** off at any time. This will make SSO optional for all users.

To fully disconnect SSO, click “Manage SSO” then “Reset connection.” This will end all users’ sessions and require them to sign back in via email login link.

---

Related Articles

[Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)[Google Workspace SSO setup](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup)[Okta SSO setup](https://support.claude.com/en/articles/13917894-okta-sso-setup)[Ping Identity SSO setup](https://support.claude.com/en/articles/13917902-ping-identity-sso-setup)[SSO login](https://support.claude.com/en/articles/14503613-sso-login)
