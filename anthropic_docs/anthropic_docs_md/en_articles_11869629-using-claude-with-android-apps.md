# Using Claude with Android Apps

**Source:** https://support.claude.com/en/articles/11869629-using-claude-with-android-apps

Claude can now connect with your Android device's system apps to help you take action directly from your conversations. When you chat with Claude, it can draft messages, emails, calendar events, set alarms and timers, find locations, and more — all through your everyday apps without copy-paste.

This feature is supported on all Claude plans and works with your device's native and third-party apps, including messaging, email, calendar, alarms, timers, location services, and maps.

# What can Claude do with Android apps?

Claude can help you:

* **Draft and send messages** through your default messaging app or third-party apps (e.g. WhatsApp, Slack, Messenger).
* **Compose emails** that open directly in your Android device's email app with content pre-filled.
* **Access your location** to provide contextual suggestions for nearby places and services.
* **Display locations on maps** and help you navigate to restaurants, stores, and other destinations.
* **Read and manage your calendar** to check availability, create events, and schedule meetings.
* **Set alarms** directly through your Clock app.
* **Set timers** directly for cooking, workouts, or any activity.

# Limitations

* **Location:** Members of Team or Enterprise plans can’t access the location tool at this time.
* **Calendar:** Ability to edit events depends on your ownership of the event.
* **Reminders:** These are exclusively available on Claude for iOS, so Claude can’t create and manage reminders on Android.
* **Contacts:** Claude does not have direct access to your contacts.

# How Claude helps you take action

When Claude determines that using one of these features would be helpful, it will automatically offer to help. You'll see a card or prompt within your conversation that lets you review and take action with Claude’s help.

**Note:** Setting alarms and timers works with voice mode beta. Other features like drafting messages and calendar events are not supported when using voice mode. See [Using voice mode on Claude Mobile Apps](https://support.anthropic.com/en/articles/11101966-using-voice-mode-on-claude-mobile-apps) for more information.

# Sending texts and emails with Messages and Mail

1. Ask Claude to help draft a message or email (for example: "Draft an email to my supervisor about the project update").
2. Claude will prepare the content and show you a preview.
3. Tap the message card to open your messaging or email app.
4. Review the pre-filled content and make any changes if needed.
5. Send the message as you normally would.

**Example:** "Draft a message to my study group about canceling tonight's session."

# Using location for contextual suggestions

1. Ask Claude for location-based recommendations (for example: "What restaurants are near me?").
2. Claude will request access to your location if not already granted.
3. Based on your location, Claude provides relevant suggestions.
4. You can view locations on a map and get navigation directions.

**Example:** "Find nearby parks for jogging."

# Displaying locations with Maps

1. When Claude suggests locations, they can be displayed on an interactive map.
2. Tap on any location to see more details.
3. Select a location to open it in Google Maps for navigation.
4. Get turn-by-turn directions directly from the map.

**Example:** "Show me hardware stores within five miles on a map."

# Managing your calendar

1. Ask Claude to check your schedule or create events.
2. Claude will request calendar access if not already granted.
3. For checking availability: Claude reads your calendar and identifies free slots.
4. For creating events: Claude prepares event details and adds them to your calendar.
5. You can edit or delete events as needed.

**Examples:**

* "What meetings do I have tomorrow?"
* "Schedule a team lunch for next Thursday at noon."
* "Create a recurring workout session every Tuesday and Thursday at 6 AM."

# Setting alarms and timers using Clock apps

1. Ask Claude to set an alarm or timer.
2. Claude will automatically create the alarm or start the timer.
3. Your device's Clock app will handle the alarm or timer.
4. You'll receive notifications as normal when the alarm goes off or timer ends.

**Examples:**

* "Set an alarm for 7 AM tomorrow."
* "Start a 20-minute timer for my workout."

# What data can Claude access?

Claude only accesses the data necessary for each specific request:

* **Location:** Current location only when relevant to your request.
* **Calendar:** Event details to check availability and create/modify events.
* **Messages/Email:** Claude does not read existing messages or emails, only creates new content.
* **Alarms and timers:** Created directly without accessing personal data.

Claude's connection to your Android apps works through your device's standard sharing system and intent system—the same secure methods used by all Android apps.

# Do I need to grant permissions to Claude for Android?

Permission requirements vary by feature:

* **Messages and Email:** No permissions required (uses Android's sharing system).
* **Calendar Events:** Claude needs your permission to read your calendar and view events, but can write to your calendar or draft calendar events using just the system UI (no permissions required).
* **Location and Maps:** Permission required when Claude needs to access your location.
* **Alarms and Timers:** Uses your device's standard alarm and timer functions.

For features requiring permissions (like location or calendar access), Claude will request permission contextually with clear explanations of why the access is needed. You’ll be prompted to approve the action with three options: Allow once, Always allow, or Don't allow.

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1707351614/ccb910e4b87b1e96ad9a11bbd835/b57b2130-d8d6-4499-89f6-6c12de236fd4?expires=1767998700&signature=66b46f87f16e8d5797858558f17f34e145fa28c4fb89fc6458e865a5feb45ad7&req=dScnEcp7nIdeXfMW1HO4zQe5FFiG0i3zS5x65TIld%2FDG5Ld5NIPFlBJCdmjn%0AzCO28PLzH3Y1Zr6vDNo%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1707351614/ccb910e4b87b1e96ad9a11bbd835/b57b2130-d8d6-4499-89f6-6c12de236fd4?expires=1767998700&signature=66b46f87f16e8d5797858558f17f34e145fa28c4fb89fc6458e865a5feb45ad7&req=dScnEcp7nIdeXfMW1HO4zQe5FFiG0i3zS5x65TIld%2FDG5Ld5NIPFlBJCdmjn%0AzCO28PLzH3Y1Zr6vDNo%3D%0A)

These permissions can be managed at any time in your device settings by going to Settings > Apps > Claude > Permissions. Click into each permission listed under **Allowed** and **Not allowed** to make changes. You can toggle between “Allow only while using the app” or “Ask every time” to change Claude’s access, or remove permissions by choosing “Don’t allow.” Claude will only request permissions if needed for specific features, and you can always choose to decline while still using other capabilities.

# Usage guidelines for optimal results

Be specific about what type of action you want Claude to take and include all relevant details like recipients, dates, times, and durations in your request. For alarms, specify AM/PM and any recurring days you need. For timers, mention what the timer is for to help with labeling. Always review content in the destination app before sending or saving.

# Troubleshooting

# Claude isn't offering to use my apps

* Make sure you're using the latest version of Claude for Android. See [How to update Claude for Android](https://support.anthropic.com/en/articles/11825394-how-to-update-claude-for-android) for instructions.
* Try being more specific about wanting to send a message, create an event, or set a timer (see examples above).
* Restart Claude for Android and try again.

# Permission prompts don't appear

* Check that the app for which Claude needs permissions is installed and set up on your phone.
* Navigate to Settings > Apps > Claude to verify that Claude for Android has the required permissions.
* Ensure your Android OS is up to date.

# Sharing options don't appear for messages or emails

* Check that you have messaging and email apps installed and set up.
* Try clearing the Claude for Android cache in your device settings:

  + Navigate to your app settings and select "Claude" from the list.
  + Select "Storage & cache."
  + Tap "Clear cache."

# Calendar events aren't opening correctly

* Verify you have a calendar app installed.
* Check that your preferred calendar app is set as the default for calendar events.
* Make sure the calendar app you’re trying to use is up to date.

# Alarms or timers aren't being created

* Ensure your device's Clock app is enabled and up to date.
* Check that "Do Not Disturb" settings aren't preventing alarms.

# Content appears different than expected

* Your Android mobile apps may format content slightly differently than Claude.
* You can always edit the content in the destination app before sending or saving.
* Some features may vary depending on your specific Android version and device manufacturer

**Need more help?** If you're experiencing issues with these features, try restarting Claude for Android or [updating the app to the latest version from the Google Play Store](https://support.anthropic.com/en/articles/11825394-how-to-update-claude-for-android).

---

Related Articles

[How can I cancel my Claude Pro subscription on Claude for Android?](https://support.claude.com/en/articles/9612898-how-can-i-cancel-my-claude-pro-subscription-on-claude-for-android)[Using the Claude Widget on Android](https://support.claude.com/en/articles/10534883-using-the-claude-widget-on-android)[Using voice mode on Claude Mobile Apps](https://support.claude.com/en/articles/11101966-using-voice-mode-on-claude-mobile-apps)[Using Claude with iOS Apps](https://support.claude.com/en/articles/11869619-using-claude-with-ios-apps)[Using Claude in Slack](https://support.claude.com/en/articles/12461605-using-claude-in-slack)
